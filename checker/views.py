from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import DomainCheck
from .forms import DomainCheckForm
from .utils import check_domain
import json


@require_http_methods(["GET", "POST"])
def checker_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = DomainCheckForm(request.POST)
        if form.is_valid():
            domain_input = form.cleaned_data.get('domain')
            
            try:
                result = check_domain(domain_input)
                
                # Save to database
                domain_check = DomainCheck.objects.create(
                    user=request.user,
                    domain=result['domain'],
                    status=result['status'],
                    ip_addresses=result['ip_addresses'],
                    registrar=result['registrar'],
                    registration_date=result['registration_date'],
                    expiry_date=result['expiry_date']
                )
                
                # Return JSON for AJAX or template context
                context = {
                    'form': form,
                    'result': result,
                    'history': DomainCheck.objects.filter(user=request.user)[:10]
                }
                
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse(result)
                
                return render(request, 'checker/index.html', context)
            except Exception as e:
                form.add_error('domain', str(e))
    else:
        form = DomainCheckForm()
    
    context = {
        'form': form,
        'history': DomainCheck.objects.filter(user=request.user)[:10]
    }
    return render(request, 'checker/index.html', context)


@login_required
def check_history(request):
    history = DomainCheck.objects.filter(user=request.user).order_by('-checked_at')[:20]
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [
            {
                'id': check.id,
                'domain': check.domain,
                'status': check.get_status_display(),
                'checked_at': check.checked_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for check in history
        ]
        return JsonResponse({'history': data})
    
    return render(request, 'checker/history.html', {'history': history})


@login_required
def check_detail(request, check_id):
    check = get_object_or_404(DomainCheck, id=check_id, user=request.user)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'id': check.id,
            'domain': check.domain,
            'status': check.status,
            'ip_addresses': check.ip_addresses,
            'registrar': check.registrar,
            'registration_date': check.registration_date,
            'expiry_date': check.expiry_date,
            'checked_at': check.checked_at.isoformat()
        })
    
    return render(request, 'checker/detail.html', {'check': check})
