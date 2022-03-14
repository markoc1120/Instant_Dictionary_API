import justpy as jp
import api
import documentation


jp.Route('/api', api.Api.serve)
jp.Route('/about', documentation.Documentation.serve)
jp.justpy()
