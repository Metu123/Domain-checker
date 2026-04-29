import requests
import json
from urllib.parse import urlparse


def clean_domain(domain):
    """Extract domain from various input formats."""
    domain = domain.strip().lower()
    
    # Remove protocol if present
    if '://' in domain:
        domain = urlparse(domain).netloc or urlparse(domain).path
    
    # Remove path if present
    domain = domain.split('/')[0]
    
    # Remove www if present
    if domain.startswith('www.'):
        domain = domain[4:]
    
    return domain


def check_dns_resolution(domain):
    """Check DNS resolution using Google DNS over HTTPS."""
    try:
        # Try Google's DNS
        url = f"https://dns.google/resolve?name={domain}&type=A"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            ips = []
            
            if 'Answer' in data:
                for answer in data['Answer']:
                    if answer.get('type') == 1:  # A record
                        ips.append(answer.get('data'))
            
            return {
                'resolved': len(ips) > 0,
                'ips': ips,
                'response_code': data.get('Status', -1)
            }
    except Exception as e:
        print(f"DNS check error: {e}")
    
    return {'resolved': False, 'ips': [], 'response_code': -1}


def check_rdap(domain):
    """Check domain registration data using RDAP."""
    try:
        # RDAP lookup
        url = f"https://rdap.org/domain/{domain}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            registrar = None
            registration_date = None
            expiry_date = None
            
            # Extract registrar
            if 'entities' in data:
                for entity in data['entities']:
                    if 'registrar' in entity.get('roles', []):
                        registrar = entity.get('handle', 'Unknown')
                        break
            
            # Extract dates
            if 'events' in data:
                for event in data['events']:
                    event_action = event.get('eventAction', '').lower()
                    event_date = event.get('eventDate', '')
                    
                    if 'registration' in event_action:
                        registration_date = event_date
                    elif 'expiration' in event_action:
                        expiry_date = event_date
            
            return {
                'registered': True,
                'registrar': registrar,
                'registration_date': registration_date,
                'expiry_date': expiry_date
            }
    except Exception as e:
        print(f"RDAP check error: {e}")
    
    return {
        'registered': False,
        'registrar': None,
        'registration_date': None,
        'expiry_date': None
    }


def check_domain(domain):
    """Perform comprehensive domain check."""
    domain = clean_domain(domain)
    
    dns_result = check_dns_resolution(domain)
    rdap_result = check_rdap(domain)
    
    # Determine status
    if dns_result['resolved']:
        status = 'active'
    elif rdap_result['registered']:
        status = 'registered'
    elif dns_result['response_code'] == 3:  # NXDOMAIN
        status = 'not_found'
    else:
        status = 'error'
    
    return {
        'domain': domain,
        'status': status,
        'ip_addresses': dns_result['ips'],
        'registrar': rdap_result['registrar'],
        'registration_date': rdap_result['registration_date'],
        'expiry_date': rdap_result['expiry_date'],
    }
