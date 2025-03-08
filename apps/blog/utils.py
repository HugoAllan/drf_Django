def get_client_ip(request):
    x_forwarded_for = request.META.get('HHTP_X_FORWARDER_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip