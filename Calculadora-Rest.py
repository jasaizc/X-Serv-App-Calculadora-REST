import webapp
import random

class calculadoraRest(webapp.webApp):
        def parse(self, request):
                peticion = request.split()[0]
                rec = request.split()[1].split("/")[1]
                cuerpo = request.split()[-1]
                return(peticion, rec, cuerpo)
        def process(self, parsedRequest):
                (peticion, rec, cuerpo) = parsedRequest
                if peticion == 'GET':
                        try:
                                if len(self.parametros.split("+")) == 2:
                                        return("200 OK", "<html>""<body><body><h1>El Resultado es: " + str(float(self.parametros.split("+")[0]) + float(self.parametros.split("-")[1])) + "</h1></body></html>")
                                if len(self.parametros.split("-")) == 2:
                                        return("200 OK", "<html>""<body><body><h1>El Resultado es: " + str(float(self.parametros.split("-")[0]) - float(self.parametros.split("-")[1])) + "</h1></body></html>")
                                if len(self.parametros.split("/")) == 2:
                                        return("200 OK", "<html>""<body><body><h1>El Resultado es: " + str(float(self.parametros.split("/")[0]) / float(self.parametros.split("/")[1])) + "</h1></body></html>")
                                if len(self.parametros.split("*")) == 2:
                                        return("200 OK", "<html>""<body><body><h1>El Resultado es: " + str(float(self.parametros.split("*")[0]) * float(self.parametros.split("*")[1])) + "</h1></body></html>")
                        except ValueError:
                                return("400 Not Found", "<html>""<body><body><h1>El Resultado Erroneo</h1></body></html>")
                        except AttributeError:
                                return("400 Not Found", "<html>""<body><body><h1>Operacion Erronea</h1></body></html>")
                                                                                   
                elif peticion == 'PUT':
                        self.parametros = cuerpo;
                        return("200 OK", "<html>""<body><body><h1>La Operacion es: " + str(self.parametros) + "</h1></body></html>")
		
		else:
                        return("400 Not Found", "<html>""<body><body><h1>Operacion Erronea</h1></body></html>")
		
if __name__ == "__main__": 
	serv = calculadoraRest("localhost", 1234) 
	
