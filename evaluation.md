# Evaluation
The document needs to describe the evaluation methodology for both the overall system as well as each individual components for the technical/user dimensions, e.g. by defining specific performance indicators that will be measured, tools that will be used.

In particular, we will evaluate 3 different aspects: 
1. Conversion rate
2. User experience
3. Technical part

## Conversion rate
We will build a landing page where we have a value proposition describing our product  with a Call To Action (CTA).
We will do this to acquire lead (people who showed interest)

Then, we will monitorize our conversion rate (#people that convert to CTA/#visitors) and we will try to optimize (CRO).

In order to measure the UX we need to have customers (or at least lead).
Hence, first of all we need to define better our Buyer Persona (demographics, values, goals, challenges)
Then, we need to measure our demand and we need to understand where our customers are gathering.
Generally, we can have 2 types of customers:
- latent demand: they are not actively seeking a solution, but they may be interested
- Demand aware: they are actively trying to solve the problem

We will use:
--  Latent demand: Facebook ADS to find our dimensions (setting charateristic of our buyer Persona)
--  Demand aware: [Ubersuggest](https://neilpatel.com/ubersuggest/) o [AnswerThePublic](https://answerthepublic.com/). 


## User Experience
We will measusre do this in 2 different way:
1 - offline part: stuff that does not scale. We will send our prototype to 3F (Family, Fools, Friends). (1)
2 - Online part: scalable: for each users. We will use automatic tools such as [HotJar](https://www.hotjar.com/) or [YandexMetrica](https://metrica.yandex.com/about) to analyze
visitors: heatmap, video recording, visiting time, conversion funnels...
In addition, we can add Incoming Feedback and Feedback pools natively included into our webapp.


Describe the situation:
### Offline part
| #    | Attribute              | Examples                                                |
| ---- | ---------------------- | ------------------------------------------------------- |
| 1    | Product                | *Artist Web app *                                                |
| 2    | Design Stage           | Concept design,                 |
| 3    | Product representation | Storyboard, Flash animation                             |
| 4    | Purpose of evaluation  | Find best design alternative                            |
| 5    | Study location         | Online study (due to COVID-19), maybe telphone          |
| 6    | Participants           | 3F,            |
| 7    | Time restrictions      | 1 week, lunch hour (from assigment to result) |
| 8    | Equipment, tools       | Phone and notes            |
| 9    | Skill of researchers   | students                  |
|      |                        |                                                         |


### Online part
| #    | Attribute              | Examples                                                |
| ---- | ---------------------- | ------------------------------------------------------- |
| 1    | Product                | *Artist Web app *                                                |
| 2    | Design Stage           | Prototype                 |
| 3    | Product representation | Storyboard, Flash animation                             |
| 4    | Purpose of evaluation  | Find best UX                            |
| 5    | Study location         | Online study        |
| 6    | Participants           | UX experts, all visitors, kids (with parents)           |
| 7    | Time restrictions      | 1 week, lunch hour (from assigment to result) |
| 8    | Equipment, tools       | Yandex Metrica: heatmap, video-recording            |
| 9    | Skill of researchers   | students                  |
|      |                        |                                                         |


The project will select one of the ideas (described by storyboards) based on four criteria:

1. Potential impact in energy saving *(in our case is different)*
2. Technical feasibility
3. Cost of the system
4. User Experience

## Technical view
From a technical point of view, we will analyze several aspects:
- **Money**: How much does our cloud based service cost us by using Machine Learning on Google cloud platform.
- **Easy installation**: How long does configuration and deployment take for a fresh installation.
- **Installation scalability**: If the installation requires specialized technicians or once configured, the installation managers can install the devices themselves.
- Possibility of OTA updates to monitor the product remotely.

In order to test our solution, we will proceed in this way:
1. Input part: STM32MP157C board + Grid-Eye sensor
2. Core part: deployed on Google Cloud Platform (IoT Core, Cloud Storage, Cloud Vision, AI Platform)
3. Artist Webapp: developed using Angular+Firebase and deployed on Firebase Hosting using Magenta   arbitrary image stylization model
4. Output part: (STM32MP157C: -> HDMI -> Projector) we use STM32MP157C that will be connected to a projector thanks to an hdmi cable.

## Offline part: done

Abbiamo concluso la parte di evaluation offline. 
Abbiamo intervistato 10 persone e questi sono i feedback:
[Feedback](users_opinion.md)

