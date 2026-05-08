from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import DomainCheck
from .forms import DomainCheckForm
from .utils import check_domain


@login_required(login_url='/accounts/login/')
@require_http_methods(["GET", "POST"])
def checker_view(request):

    form = DomainCheckForm()

    if request.method == 'POST':
        form = DomainCheckForm(request.POST)

        if form.is_valid():
            domain_input = form.cleaned_data['domain']

            try:
                result = check_domain(domain_input)

                DomainCheck.objects.create(
                    user=request.user,
                    domain=result['domain'],
                    status=result['status'],
                    ip_addresses=result['ip_addresses'],
                    registrar=result['registrar'],
                    registration_date=result['registration_date'],
                    expiry_date=result['expiry_date']
                )

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse(result)

                return render(request, 'checker/index.html', {
                    'form': form,
                    'result': result,
                    'history': DomainCheck.objects.filter(user=request.user)[:10]
                })

            except Exception as e:
                form.add_error('domain', str(e))

    return render(request, 'checker/index.html', {
        'form': form,
        'history': DomainCheck.objects.filter(user=request.user)[:10]
    })


@login_required(login_url='/accounts/login/')
def check_history(request):
    history = DomainCheck.objects.filter(user=request.user).order_by('-checked_at')[:20]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [
            {
                'id': c.id,
                'domain': c.domain,
                'status': c.get_status_display(),
                'checked_at': c.checked_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for c in history
        ]
        return JsonResponse({'history': data})

    return render(request, 'checker/history.html', {'history': history})


@login_required(login_url='/accounts/login/')
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
