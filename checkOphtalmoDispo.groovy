#!/usr/bin/env groovy

@Grapes([
    @Grab('org.codehaus.groovy.modules.http-builder:http-builder:0.7.2')
])

import groovyx.net.http.HTTPBuilder
import groovyx.net.http.Method

String DOCTOLIB_API_URL = "https://partners.doctolib.fr"

HTTPBuilder http = new HTTPBuilder(DOCTOLIB_API_URL)
http.setProxy('gateway.oxylane.zscaler.net', 80, 'http')

Map<String, String> queryParams = [
                            "agenda_ids" : "9765-10984-2316-2317-2318-2319-2320-2322-2323-2324-2325-2328-2329-2330-2326-2566-2321-2379-2314",
                            "insurance_type" : "",
                            "limit" : "15"
                        ]

http.request(Method.POST) { req ->
    uri.path = "/availabilities/12498/2016-06-23"
    uri.query = queryParams

    response.success = { resp, xml ->
        assert resp.statusLine.statusCode == 201
        println("${xml}")
    }

    response.failure = { resp ->
        String error = ((groovyx.net.http.HttpResponseDecorator) resp).context.delegate.toString().replace(',', ',\n')
        println("ERROR : ${error}")
    }
}
