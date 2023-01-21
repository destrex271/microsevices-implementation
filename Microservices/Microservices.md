Microservice based architecture refers to the design philosophy which aims to break down a particular application into smaller loosely coupled units. These units are supposed to be independent of each other, working as a seperate entities but in a cohesive manner.
These smaller units are what we call a **microservice**.

### Why do we need microservices?
For this we need to understand what came before and what were its drawbacks that led us to go for a microservice based architecture. The earlier architecture pattern was known as monolithic architecture.
As the name suggests in this all the parts of the application ran together and were dependent on each other. If a particular service goes down it might affect other services as well and because of this high level of dependency this architecture method often leads to frequent failures.

## Pilars of Microservices
1. Highly cohesive and loosely coupled
	Cohesion in terms of microservices mean how well the various microservices work together.
	Low coupling means that two unrelated services should be kept seperate from each other.
2. Discrete Boundaries
	Avoid having cross functional dependencies between microservices. Eg: If we have a service for authentication and authorization and another for user profile, the profile service should not call the authorization service before executing its own function.
3. Single Responsibility principle to facilitate updates
	According to this principle there should only be a single reason to update the microservice *i.e* when updating a microservice the changes should be minimal and that is possible only if it is of the optimal size.
4. Design for Failure
	Goes hand in hand with the curcuit breaker design pattern which works by controlling the flow of failure whenever it occurs. In case of microservices this can be implemented when a particular service goes down for eg a database service but the application service keeps on working without being affected. We can easily stop the communication that was happening between the two services earlier.
5. Buisiness/Task Capability
	According to this a microservice should handle only a particular single *buisiness/task* properlyto improve performance and reduce the chances of failure. This helps in ensuring scalability.
6. 