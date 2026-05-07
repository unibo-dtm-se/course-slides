
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

{{% section %}}

## Check your understanding (pt. 1)

- TBD

{{% /section %}}

---

{{% import path="reusable/back.md" %}}