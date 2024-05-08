
Example Request Body:
{
    "url": "https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
    "question": "What are the concerns around Generative AI?"
}

Example:

(I have used powershell)

StatusCode        : 200
StatusDescription : OK
Content           : {
                      "answer": "There's been apprehension regarding the possible misapplication of generative AI, including its involvement in cybercrime, dissemination of fake news or deepfakes to deceive or manipulate individuals, and the widespread displacement of human employment."
                    }
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 195
                    Content-Type: application/json
                    Date: Wed, 08 May 2024 13:38:37 GMT
                    Server: Werkzeug/2.3.6 Python/3.11.3

                    {
                      "answer": "There's been apprehension regarding the possible misapplication of generative AI, including its involvement in cybercrime, dissemination of fake news or deepfakes to deceive or manipulate individuals, and the widespread displacement of human employment."
                    }
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 195], [Content-Type, application/json], [Date, Wed, 08 May 2024 13:38:37 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 195
