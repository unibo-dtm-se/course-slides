
+++

title = "Web, ReST, and Web Services"
description = "Web Services and RESTful APIs"
outputs = ["Reveal"]

+++

# Web Services and RESTful APIs

{{% import path="reusable/header.md" %}}

<!-- ## TOC

1. What is the Web
    + Web $\approx$
        - a distributed hypermedia information system
        - a collection of resources (documents, data, services) accessible via the Internet and linked by hyper links
        - an infrastructure for distributed systems based on the HTTP protocol
    + URLs
    + HTTP protocol
        1. messages (requests and responses)
        2. methods (GET, POST, PUT, DELETE, etc.)
        3. status codes (200, 404, 500, etc.)
    + HTML (structure + content), JavaScript (behaviour), and CSS (styling)
    + Hypermedia, hypertext, (links)
2. History of the Web in a nutshell
    1. Web 1.0: static pages, read-only
    2. Web 2.0: dynamically generated pages + template engines
    3. Web 3.0: dynamic pages using AJAX to contact Web Services
    4. Web 4.0: single pages applications (SPA)
3. What are Web Services
    + a sort of Distributed object with an HTTP interface, accessible over the Web, encapsulating functionalities and data, and reusable by different clients
    + API of a Web Service: end points + input parameters and data formats + output data formats + status codes
4. Web Services as the Backbone of Modern Distributed Systems
    + Web mechanisms are simple to understand, yet incredibly flexible and versatile
    + Web is pervasive (and highly optimized)
    + Web is highly compatible with virtually any programming language and platform
    + Web has very low entry barrier (HTTP is simple, widely supported, and firewall-friendly)
    + ReST architectural style makes Web the best technological stack for most DS
    + WS may easily wrap legacy software in order to:
        - expose it to the Web hence turning concentrated software into distributed software
        - allow interoperability among heterogeneous software components
5. The "ReST" Architecture Style
    1. client–server architecture (servers host resources, clients access them, possibly via proxies)
    2. representational state transfer (only representations of (states of) resources are transferred between client and server)
    3. uniform interface (resources are identified by URLs, and manipulated through a fixed set of operations, e.g., HTTP methods)
    4. stateless interactions (each request from client to server must contain all the information needed to understand and process the request, and cannot rely on any stored context on the server)
    5. cacheable responses (clients can cache responses to improve performance)
    6. layered system (a client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way)
    7. code on demand (servers can temporarily extend or customize the functionality of a client by transferring executable code)
6. ReSTful APIs in Practice
    1. Think the system in terms of i. collections of resources, ii. resources, iii. operations admissible onto resources
    2. Devise Web APIs, e.g. via OpenAI specification (OAS)
        1. identify end points and their parametric URLs
        2. identify admissible HTTP operations
        2. identify input parameters and data formats
        3. optionally identify input HEADERs
    3. Implement Web APIs server side, e.g. via Flask, FastAPI, Spring Boot, etc.
    4. Implement frontend so to leverage Web APIs, e.g. via React, Angular, Vue, etc.
7. Anatomy a Web Project (backend + static JS)
    - simple flask project with HTML templates and static JS, CSS, and media files
    - let the students reflect on the fact that the project organization is poor, most likely there will be tests only for the backend
8. Anatomy a Web Project (frontend + backend + API gateway)
    - Python project for backend + JS project for frontend + API gateway (e.g., Nginx)
    - better suited for SPA
    - frontend can have its own testing
    - integration tests are necessary
    - possibly each sub-project may have its own versioning and release cycle
-->

---

# What is the Web?

The Web is, at the same time:

- a __distributed__ _hypermedia_ information system
- a collection of __linked__ _resources_ accessible via the _Internet_ (in particular, via _HTTP_)
- an _infrastructure_ for __distributed systems__ based on _HTTP_

{{% fragment %}}

In practice, the Web revolves around:

- resources __identified__ by _URLs_
- interactions __mediated__ by _HTTP_
- documents and applications __built__ with _HTML_, _CSS_, and _JavaScript_
- _hyperlinks_ __connecting__ information and behaviour

{{% /fragment %}}

---

## Hyper-links, hyper-text, and hyper-media

- __hyper-links__ are _references_ from one resource to another, enabling navigation and discovery
- __hyper-text__ is text that contains links to other text
- __hyper-media__ generalizes the concept to include links in images, audio, video, forms, etc.
- the Web's success is largely due to its ability to connect resources through links
    + in the user's perspective, the Web is something to _navigate_ and _explore_ through links...
    + ... not just a collection of isolated documents

---

## URLs identify resources

<!-- ![Annotated URL diagram showing scheme, subdomain, domain, top-level domain, port, path, query string, and fragment identifier](./http-url.png) -->
{{< image max-h="80vh"  src="./http-url.png" alt="Annotated URL diagram showing scheme, subdomain, domain, top-level domain, port, path, query string, and fragment identifier" >}}
<br>

- a URL tells the client where a resource is and how to reach it
- different parts of the URL may identify host, port, path, query parameters, or fragment
- in ReSTful systems, URLs should identify resources rather than actions
    + e.g. WRONG URL: `https://example.com/getCustomer?id=123`
    + e.g. RIGHT URL: `https://example.com/customers/123`

---

{{% section %}}

## HTTP is the Web's application protocol

__Hyper-Text Transfer Protocol__ (_HTTP_) standardizes how clients and servers exchange messages:

{{< image max-h="50vh" src="./http-ingredients.svg" alt="Diagram showing HTTP request and response messages with headers and body" >}}

1. _clients_ acting on behalf of users or applications
0. _servers_ hosting resources or providing functionalities
0. _requests_ from client to server
0. _responses_ from server to client
0. _methods_ describing the intended operation
0. _status codes_ describing the outcome
0. _headers_ and _bodies_ carrying metadata and content

---

## Example of simple HTTP interaction (read)

1. Client wants to remotely _read_ volume of a speaker (id: `123`), hosted by server at `https://example.com`
2. Server allows users to _read_/change volume of speakers, by speaker ID, through HTTP
3. To read the volume, client sends an HTTP _request_ to URL `https://example.com/speakers/123/volume`
    - method: `GET` ["I want to read some information about the resource"]
    - headers:
        * `Accept: text/html` ["I want the response to be an HTML page describing the volume"]
        * `Authorization: <auth token here>` ["I am authorized to access this resource, here is my token"]
    - body: (empty)
4. Server processes the request, reads the actual volume value, and produces a Web page describing that speaker's volume, sending back an HTTP _response_
    - status code: `200 OK` ["The request was successful, here is the information you asked for"]
    - headers:
        * `Content-Type: text/html` ["The body of this response is an HTML document"]
        * `Cache-Control: no-cache` ["Don't cache this response, it may change frequently"]
    - body: `<html><body><h1>Speaker 123</h1><p>Volume: 75%</p></body></html>` ["Here is the HTML page describing the speaker's volume"]

---

## Example of simple HTTP interaction (write)

1. Client wants to remotely _increase_ volume of a speaker (id: `123`), hosted by server at `https://example.com`
2. Server allows users to read/_change_ volume of speakers, by speaker ID, through HTTP
3. To increase the volume, client sends an HTTP _request_ to URL `https://example.com/speakers/123/volume`
    - method: `POST` ["I want to change some information about the resource"]
    - headers:
        * `Content-Type: application/json` ["The body of this request is a JSON document describing the change I want to make"]
        * `Authorization: <auth token here>` ["I am authorized to access this resource, here is my token"]
    - body: `{"change": "+10%"}` ["I want to increase the volume by 10%"]
4. Server processes the request, updates the actual volume value, and sends back an HTTP _response_
    - status code: `204 No Content` ["The request was successful, but there is no content to return in the body"]
    - headers: (none)
    - body: (empty)

{{% /section %}}

---

## HTTP request messages

<!-- ![Diagram of an HTTP request showing request line, headers, blank line, and optional entity body](./http-req.png) -->
{{< image max-h="70vh" src="./http-req.png" alt="Diagram of an HTTP request showing request line, headers, blank line, and optional entity body" >}}

- __Method__: what to do on the resource (e.g., GET, POST, PUT, DELETE)
- __URL__: what resource to access and where (e.g., https://example.com/speakers/123/volume)
- __Headers__: metadata about the request (e.g., format of the body, authentication token, requested response format, etc.)
- __Body__: optional content sent to the server (e.g., requested changes to the resource, etc.)
- \[Protocol\] __Version__: necessary to let older and newer client/servers interoperate

---

## HTTP response messages

<!-- ![Diagram of an HTTP response showing status line, headers, blank line, and optional entity body](./http-res.png) -->
{{< image max-h="70vh" src="./http-res.png" alt="Diagram of an HTTP response showing status line, headers, blank line, and optional entity body" >}}

- __Status code__: numeric code identifying the success or failure of the request (e.g., 200, 404, 500)
- __Reason phrase__: human-readable description of the status code (e.g., "OK", "Not Found", "Internal Server Error")
- __Headers__: metadata about the response (e.g., format of the body, caching directives, etc.)
- __Body__: optional content sent to the client (e.g., requested information, error message, etc.)
- \[Protocol\] __Version__: necessary to let older and newer client/servers interoperate

---

## About HTTP methods

_Standard_ set of admissible operations that clients may request on resources:

- main ones: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`

    ![Table mapping HTTP verbs to CRUD operations for collections and specific resources](./http-methods.png)

- many more are supported, for example `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`, etc.
    * see https://developer.mozilla.org/docs/Web/HTTP/Methods for a complete list

---

## About HTTP status codes

<!-- ![Chart grouping common HTTP status codes into success, client error, and server error classes](./http_status_codes.png) -->
{{< image max-h="70vh" src="./http_status_codes.png" alt="Chart grouping common HTTP status codes into success, client error, and server error classes" >}}

- 3-digit, positive integer numbers, the most significant digit identifying the class of the response:
    + `1xx`: informational responses (e.g., "time to swap to another protocol")
    + `2xx`: successful responses (e.g. "successfully processed the request with/without body being returned")
    + `3xx`: redirection messages (e.g. "the resource has moved, here is the new URL")
    + `4xx`: client-side error responses (e.g. "cannot process the request due to client's mistake")
    + `5xx`: server-side error responses (e.g. "cannot process the request due to server's mistake")

- most common status codes are in the picture:
    + see https://developer.mozilla.org/docs/Web/HTTP/Status for a complete list

---

## About HTTP headers

Key–value pairs that carry metadata about the request or response, for example:

- `Content-Type`: specifies the media type of the body content \[both in reqs and resps\]
- `Authorization`: contains credentials for authenticating the client \[commonly in reqs\]
- `Cache-Control`: provides directives for caching mechanisms \[commonly in resps\]
- `Accept`: indicates the media types that the client can process \[commonly in reqs\]
- `Set-Cookie`: instructs the client to store a cookie \[commonly in resps\]
- `User-Agent`: identifies the client software making the request \[commonly in reqs\]
- `Location`: indicates the URL of a newly created resource or a redirection target \[commonly in resps\]
- full list of standard headers: https://developer.mozilla.org/docs/Web/HTTP/Headers

{{% fragment %}}

> Server designers may "invent" _custom headers_, but it's best to stick to standard ones when possible for better interoperability
- custom headers should be prefixed with `X-` to avoid conflicts with standard headers
    + but this convention is being deprecated in favor of using a custom namespace (e.g., `MyApp-`) for non-standard headers.

{{% /fragment %}}

---

## Content format ("type") negotiation

Clients and servers may automatically _negotiate_ the format of the data being exchanged

- Assumtion:
    1. the server may represent resources in various formats (e.g., HTML, JSON, XML, etc.)
    2. the client may prefer certain formats over others (e.g., a browser may prefer HTML, while an API client may prefer JSON)
- Mechanism:
    1. client sends an `Accept` header listing the media types it can process, possibly with quality values (e.g., `Accept: text/html, application/json;q=0.9, */*;q=0.8`)
    2. server selects the best format it can produce based on the client's preferences and its own capabilities
    3. server sends the response with the selected format and a `Content-Type` header indicating the media type of the body (e.g., `Content-Type: application/json`)
    4. client processes the response according to the specified format
- "Formats" are expressed as _media types_ (also known as __MIME types__), which are standardized identifiers for data formats (e.g., `text/html`, `application/json`, `image/png`, etc.)

---

## About MIME types

1. MIME stands for "Multipurpose Internet Mail Extensions", but it is used far beyond email to identify media types in HTTP and other protocols

2. A MIME type consists of a type and a subtype, separated by a slash (e.g., `text/html`, `application/json`, `image/png`)

3. Full list is available at https://developer.mozilla.org/docs/Web/HTTP/Guides/MIME_types/Common_types

4. Most common MIME types are in the table below:

    <!-- ![Table of MIME type families including text, image, audio, video, and application with examples](./mime_types.png) -->
    {{< image max-h="50vh" src="./mime_types.png" alt="Table of MIME type families including text, image, audio, video, and application with examples" >}}

---

{{% section %}}

## Most common Web content types (pt. 1)

- [Hypertext Markup Language](https://html.spec.whatwg.org/) (_HTML_): `text/html` (for Web pages) should describe the content of a Web page, with no stylistic or behavioural information
    + "the page" usually represents some resource (physical, digital, or virtual) that exists on the server-side, in a human-friendly way
    + it may contain links to other resources (e.g. media, other pages, scripts, etc.)
    + it may contain forms to let users interact with the server (e.g. submit data, trigger actions, etc.)
    + it may contain identifiers (e.g. `id` attributes) and classes for page contents (e.g. paragraphs, buttons, etc)
        * so that CSS and JavaScript can refer to them for styling and behaviour purposes
    + underlying assumption is that the client knows how to render HTML pages...
        * ... after downloading and interpreting all the resources linked from the page (e.g. CSS, JS, media, etc.)

    + example of HTML page describing a speaker resource:

    ```html
    <html>
        <body>
            <h1>Speaker 123</h1>
            <p>Volume: 75%</p>
            <button id="increase-btn">Increase Volume</button>
        </body>
    </html>

---

## Most common Web content types (pt. 2)

- [Cascading Style Sheets](https://www.w3.org/Style/CSS/specs.en.html) (_CSS_): `text/css` (for stylesheets) should describe the styling of a Web page, with no content or behaviour information
    + it may contain rules about how to depict individual elements or groups of elements of the page (as identified by their tag, id, class, etc.)
    + these rules are interpreted by the client to determine how to render the page (e.g. colors, fonts, layout, etc.)

    + example of CSS stylesheet describing the styling of a speaker page:

    ```css
    /* file styles.css */
    body { font-family: Arial, sans-serif; background-color: #f0f0f0; }
    h1 { color: #333; }
    p { font-size: 18px; }
    #increase-btn { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
    #increase-btn:hover { background-color: #45a049; }
    ```

---

## Most common Web content types (pt. 3)

- [JavaScript](https://developer.mozilla.org/docs/Web/JavaScript) (_JS_): `application/javascript` (for scripts) should describe the behaviour of a Web page, with no content or styling information
    + it may contain instructions to manipulate the content and styling of the page (e.g. by adding, removing, or changing elements, classes, attributes, etc.)
    + such instructions may be triggered by events occurring after the page has been shown to the user (e.g. button clicks, form submissions, etc.)
    + such instructions are provided by the server, along with the page, to let the client know how to "animate" the page and make it interactive

    + example of JavaScript code reloading the page when the "Increase Volume" button is clicked:

    ```javascript
    // file script.js
    document.getElementById('increase-btn').addEventListener('click', function() {
        location.reload();
    });

---

## Most common Web content types (pt. 4)

__Wrap-up:__ most commonly the HTML pages contains references to the CSS and JS files that describe the styling and behaviour of the page, respectively, and the client is responsible for downloading and interpreting all these resources to render the page correctly:

```html
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="styles.css"> <!-- reference to CSS stylesheet -->
        <script src="script.js"></script>                         <!-- reference to JavaScript file -->
    </head>
    <body>
        <h1>Speaker 123</h1>
        <p>Volume: 75%</p>
        <button id="increase-btn">Increase Volume</button>
    </body>
</html>
```

---

## Most common Web content types (pt. 4)

- [JavaScript Object Notation](https://www.json.org/) (_JSON_): `application/json` (for data exchange) should describe the content of a resource in a machine-friendly way, with no styling or behaviour information
    + it may contain structured data representing the state of a resource, or the result of an operation on a resource, etc.
    + \[[AJAX](https://en.wikipedia.org/wiki/Ajax_(programming))\] sometimes the JS code may contact the server to get some tiny piece of information in JSON format, rather than the entire HTML page, in order to update the page dynamically without reloading it
    + other times, the client is not a browser, but some software component that just needs data in machine-friendly format

    + example of JSON document describing a speaker resource:

    ```json
    {
        "id": 123,
        "name": "Living Room Speaker",
        "volume": 75,
        "status": "on"
    }
    ```

    + example of JavaScript code exploiting AJAX to contact the server and update the page dynamically:

    ```javascript
    document.getElementById('increase-btn').addEventListener('click', function() {
        // Send an AJAX request to the server to increase the volume
        fetch('/speakers/123/volume', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ change: '+10%' })
        }).then(response => {
            if (response.ok) {
                // If the request was successful, update the volume displayed on the page
                let volumeElement = document.querySelector('p');
                let currentVolume = parseInt(volumeElement.textContent.split(': ')[1]);
                volumeElement.textContent = `Volume: ${currentVolume + 10}%`;
            } else {
                alert('Failed to increase volume');
            }
        });
    });
    ```

---

## Most common Web content types (pt. 3)

- other common formats, conceptually equivalent to JSON, include:
    + __eXtensible Markup Language__ (_XML_): `application/xml` (for data exchange) a sort of generalization of HTML, with custom tags and no predefined semantics:

    ```xml
    <speaker>
        <id>123</id>
        <name>Living Room Speaker</name>
        <volume>75</volume>
        <status>on</status>
    </speaker>
    ```

    + __YAML Ain't Markup Language__ (_YAML_): `application/x-yaml` (for data exchange) a sort of generalization of JSON, with more human-friendly syntax (easier to read and write):

    ```yaml
    id: 123
    name: Living Room Speaker
    volume: 75
    status: on
    ```


{{% /section %}}

---

## History of the Web in a nutshell

1. Web 1.0: mostly static pages, read-only browsing
2. Web 2.0: server-side dynamic pages, forms, template engines, user-generated content
3. Web 3.0: rich clients using AJAX to talk to Web services asynchronously
4. Web 4.0: single-page applications with highly interactive frontends

![Timeline or comparison figure showing Web 1.0 static pages, Web 2.0 dynamic server-rendered pages, Web 3.0 AJAX-based applications, and Web 4.0 single-page applications](./web-evolution.png)

---

## What are Web Services?

A Web service is, roughly speaking:

- a distributed software component exposed through an HTTP interface
- accessible over the network by heterogeneous clients
- designed to encapsulate data and functionality behind a stable API

Its API typically specifies:

- endpoints and URL patterns
- admissible HTTP methods
- input parameters, headers, and body formats
- output formats and status codes

![Architecture figure showing multiple clients such as browser, mobile app, and backend service calling the same HTTP web service](./web-service-overview.png)

---

## Why Web Services dominate distributed systems

Web services are the backbone of modern distributed systems because:

- Web mechanisms are simple yet flexible
- HTTP is pervasive and highly optimized
- the Web stack is language- and platform-independent
- HTTP is widely supported and usually firewall-friendly
- ReST encourages interoperability through a uniform interface

They are also useful to wrap legacy software so as to:

- expose existing capabilities on the Web
- let heterogeneous components interoperate

![Figure showing a legacy system wrapped by a web API so browsers, apps, and other services can access it over HTTP](./legacy-to-web-service.png)

---

## The ReST architectural style

ReST is an architectural style for distributed hypermedia systems.

Its key constraints are:

1. client-server
2. representational state transfer
3. uniform interface
4. stateless interactions
5. cacheable responses
6. layered system
7. code on demand

The point is not to use HTTP superficially, but to structure interactions around resources and representations.

---

## ReST constraints in practice

1. client-server: clients consume resources, servers host them
2. representation-oriented: clients exchange representations, not direct access to server internals
3. uniform interface: resources are identified by URLs and manipulated via standard HTTP methods
4. stateless: each request contains all the information needed to process it
5. cacheable: responses may be reused when allowed
6. layered: proxies, gateways, and intermediaries can be inserted transparently
7. code on demand: optional transfer of executable code, for example JavaScript

![Diagram showing clients, proxies, cache, API gateway, and origin server to illustrate client-server, statelessness, caching, and layers in REST](./rest-constraints-overview.png)

---

## ReSTful APIs in practice

Design the system in terms of:

1. collections of resources
2. individual resources
3. admissible operations on each resource

Typical reasoning pattern:

- collection endpoint: /customers
- item endpoint: /customers/{id}
- operation semantics mapped onto HTTP methods

![Table mapping GET, POST, PUT, PATCH, and DELETE to resource collections and single resources in a REST API](./http-methods.png)

---

## From API design to implementation

1. devise the API, for example with OpenAPI Specification
2. identify endpoints and parametric URLs
3. identify admissible HTTP operations
4. identify input parameters and body formats
5. optionally define relevant headers
6. define response formats and status codes

Then implement:

- the server side with frameworks such as Flask, FastAPI, or Spring Boot
- the frontend side with frameworks such as React, Angular, or Vue

![Figure showing workflow from resource modeling to OpenAPI description to backend implementation to frontend consuming the API](./api-design-to-implementation.png)


---

{{% section %}}

## Check your understanding (pt. 1)

- What does it mean to say that the Web is a distributed hypermedia information system?
- What is the role of a URL in Web communication?
- Which parts make up an HTTP request? And an HTTP response?
- What is the difference between an HTTP method and an HTTP status code?
- What are HTML, CSS, and JavaScript responsible for in a Web application?
- What is the difference between hypertext and hypermedia?
- How did the Web evolve from static pages to single-page applications?
- What is a Web service, and how is its API usually described?
- Why are Web services so effective for distributed systems integration?
- What are the main constraints of the ReST architectural style?
- What does it mean for a ReST interaction to be stateless?
- How would you model a simple domain in terms of collections, resources, and operations?

{{% /section %}}

---

{{% import path="reusable/back.md" %}}