# Final Evaluation

Once the project have been finished, we performed some tests, in order to evaluate both the technical quality of the work and the user experience.



#### Technical part





To do this, we first tried to run private tests (between the member of the group) in two ways: initially "black box" tests on **small parts** of the architecture, to monitor single tasks of the project, in some cases also simulating the parts not in exam:

- Input part: regarding ESP32, I2C, Grid-Eye connection wires, ports, RIOT code
- Core part: deployment on Google Cloud, correct usage of GCloud Storage, Pub/Sub, Cloud Run, ecc.
- Web Application: Firebase and Angular development
- Output part: we had not the possibility of using a projector, but we displayed the final result on a monitor.


and then we tried with the entire architecture running. 





At the start of the implementation phase, we were focused on an edge deployment. We tried to do the part of image processing on our Raspberry PI, but the results were awful: because of the low computational power, an entire flow of data, from the grid eye to the image displayed, took about 10 minutes, an unthinkable time. We tried different images, with the hope that the time could depend from the size, but the results were bad, again. So we moved to a cloud approach: here we give a sketch of our tests. We tested different images with both approaches, and the table shows the time of execution.



*TABELLA*







As we can see, the final results are good: the architecture cloud-based, despite the **complexity**, performs well in all tasks we designed, and the flow of data is linear. To execute an entire run, from the collection of data to the final result, we need just some seconds, that should be a good result given that we pass through a lot of different nodes during the run.



Moreover, with the actual configuration, we are not experiencing **any expenses** for traffic consumption, that would increase in the case of modification of the image processing.



Finally, we can conclude that all the goals for a minimum valuable product that we have set ourselves have been satisfied; in the future, we could extend the project with the use of a solid machine learning processing and the insertion of different ways for data collection



#### User experience





About the user experience, with respect to our initial plans, we can say that we carried out the offline part: we gave the web application to about 20 people, where they loaded an image of their choice, and we collected opinions about the difficulty of the actions, and the satisfaction about the final result provided by our architecture. 



Our testers compiled a survey about the application: it turned out that almost all of them have been happy about the easiness with which it is possible to approach to the application, and a majority of people have been **satisfied** also by the final artwork, saying that they expected exactly something like the result given.



Concerning the online part and the conversion rate of the initial evaluation plan, it is part of our future plans.





