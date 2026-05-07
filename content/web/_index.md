
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

- a distributed hypermedia information system
- a collection of resources accessible via the Internet
- an infrastructure for distributed systems based on HTTP

In practice, the Web revolves around:

- resources identified by URLs
- interactions mediated by HTTP
- documents and applications built with HTML, CSS, and JavaScript
- hyperlinks connecting information and behaviour

---

## URLs identify resources

![Annotated URL diagram showing scheme, subdomain, domain, top-level domain, port, path, query string, and fragment identifier](./http-url.png)

- a URL tells the client where a resource is and how to reach it
- different parts of the URL may identify host, port, path, query parameters, or fragment
- in ReSTful systems, URLs should identify resources rather than actions

---

## HTTP is the Web's application protocol

HTTP standardizes how clients and servers exchange messages:

1. requests from client to server
2. responses from server to client
3. methods describing the intended operation
4. status codes describing the outcome
5. headers and bodies carrying metadata and content

---

## HTTP request messages

![Diagram of an HTTP request showing request line, headers, blank line, and optional entity body](./http-req.png)

- request line: method, target URL, protocol version
- headers: metadata such as content type, authorization, cache directives
- body: optional payload, common in POST, PUT, and PATCH

---

## HTTP response messages

![Diagram of an HTTP response showing status line, headers, blank line, and optional entity body](./http-res.png)

- status line: protocol version, status code, reason phrase
- headers: metadata such as content type, caching, or location
- body: the representation of the requested resource, or error details

---

## Methods and status codes

![Table mapping HTTP verbs to CRUD operations for collections and specific resources](./http-methods.png)

![Chart grouping common HTTP status codes into success, client error, and server error classes](./http_status_codes.png)

- methods such as GET, POST, PUT, PATCH, DELETE define the operation semantics
- status codes such as 200, 201, 204, 404, 409, 500 summarize the result
- together, methods and status codes form the vocabulary of Web APIs

---

## Content on the Web

The classic Web stack separates concerns:

- HTML for structure and content
- CSS for presentation and styling
- JavaScript for dynamic behaviour

HTTP bodies can carry many media types, not just HTML pages.

![Table of MIME type families including text, image, audio, video, and application with examples](./mime_types.png)

---

## Hypertext and hypermedia

- hypertext means documents contain links to other documents
- hypermedia generalizes the same idea to images, audio, video, forms, and executable behaviour
- the Web became successful because resources are loosely coupled and navigable through links

> Links are what transform isolated documents into an information space.

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