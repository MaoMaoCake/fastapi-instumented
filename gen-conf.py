def print_config():
    config = r'''
    otelcol.processor.filter "app%s" {
        error_mode = "ignore"
        
        traces {
            span = [
                "not ( IsMatch(resource.attributes[\"service.name\"], \"fastapp%s\"))",
            ]
        }
        
        output {
            metrics = [otelcol.exporter.otlp.tempo%s.input]
            logs    = [otelcol.exporter.otlp.tempo%s.input]
            traces  = [otelcol.exporter.otlp.tempo%s.input]
        }
    }
    
    otelcol.exporter.otlp "tempo%s" { // this sends data to tempo
        client {
            endpoint = "grafana-tempo.opstella-monitoring.svc.cluster.local:4317" // internal tempo svc
            headers = {
                "X-Scope-OrgID" = "opstella%s",
            }
            tls {
                insecure             = true
                insecure_skip_verify = true
            }
        }
    }
    '''
    # print([ 1 for _ in range(7)])
    print("".join([config % (i,i,i,i,i,i,i) for i in range(1000)]))

def print_outputs():
    print(str([f"otelcol.processor.filter.app{i}.input" for i in range(1000)]).replace("'", ''))

# print_config()
print_outputs()