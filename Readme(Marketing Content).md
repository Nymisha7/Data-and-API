To use the Marketing Content Generator API, follow these steps:

Firstly,Send a POST request to the /generate-content endpoint with JSON data containing the topic and format.

Example Request Body:
{
    "topic": "Generative AI",
    "format": "linkedin"
}

You will receive the generated marketing content in the response.

Example:(Response I have received)
(I have used powershell)
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "content": "Excited to 
                    share insights on
                    Generative AI!
                    \ud83d\ude80 With its       
                    innovative capabilities,    
                    Generative AI is
                    revolutionizing various     
                    industries, from creative   
                    arts to healthcare. Its     
                    po...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 485
                    Content-Type:
                    application/json
                    Date: Wed, 08 May 2024      
                    13:38:37 GMT
                    Server: Werkzeug/2.3.6      
                    Python/3.11.3

                    {
                      "content": "Excited to    
                    share i...
Forms             : {}
Headers           : {[Connection, close],       
                    [Content-Length, 485],      
                    [Content-Type,
                    application/json], [Date,   
                    Wed, 08 May 2024 13:38:37   
                    GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass    
RawContentLength  : 485

The example output demonstrates a successful response from the API, containing the generated marketing content in JSON format.
