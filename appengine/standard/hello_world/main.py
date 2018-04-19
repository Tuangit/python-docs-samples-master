import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        # build a list of operations
        f = {'+': lambda x, y: str(float(x) + float(y)),
             '-': lambda x, y: str(float(x) - float(y)),
             '*': lambda x, y: str(float(x) * float(y)),
             '/': lambda x, y: str(float(x) / float(y)),
             'C': lambda x, y: "",
            }
        # get page parameters
        x = self.request.get('x')
        y = self.request.get('y')
        operator = self.request.get('operator')
        # calculate 
        result = ""
        try:
            result = f[operator](x, y)
        except ValueError:
            result = "Error: Incorrect Number"
        except ZeroDivisionError:
            result = "Error: Division by zero"
        except KeyError:
            pass
        # build HTML response
        buttons = "".join(["<input type='submit' name='operator' value='"
                           + o + "'>" for o in sorted(f.keys())])
        self.response.out.write("""<html>
            <body>
            <form action='/' method='get' autocomplete='off'> 
            <input type='text' name='x' value='%s'/><br/>
            <input type='text' name='y'/><br/> 
            %s 
            </form>
            </body>
            </html>""" % (result, buttons))
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
