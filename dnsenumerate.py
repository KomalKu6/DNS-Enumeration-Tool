import dns.resolver
target = "youtube.com"
records= ["A", "AAAA", "MX", "NS", "CNAME", "TXT", ""] 
resolver = dns.resolver.Resolver()
for record in records:
    try:
        answers = resolver.resolve(target, record)
    except  dns.resolver.NoAnswer:
        continue
    print(f"{record} records for {target}:")
    for data in answers:
        print(f'{data}')
        