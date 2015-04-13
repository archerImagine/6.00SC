# MIT 6.00SC | Lecture 20 | More Clustering #

## [Feature Vector ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=93) ##

In the last lecture, we saw example and the notion of clustering, In clustering we used linkage criteria to get the clusters. Now if we use a wrong linkage criteria, we might not get an optimal answer.

One more concept we studies or rather brushed through is **Feature Vector**. So we start with the concept that in place of generalizing just based on one feature, to being able to generalize based on a Feature Vector.

If all the feature in a feature vector are represented by the same physical units, we might find that easier ways of identifying the generalization.

In case a feature vector contains feature which cannot be represented in the same physical units ex. a feature vector containing, distance between cities and their temperature, then we have an issue of generalizing the feature vector.

So if we are using different physical unit for feature representation in a feature vector, we might have to think about **how to scale the elements of the vector.**

### [Scaling ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=259) ###

Scaling is not only required when we have different physical unit of representation of feature in a feature vector, It is even important when we have the same physical unit.

Consider the image in lecture slide [page 2](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20_slides.pdf), in which both height and width, are presented in inches. So if we scale based on height the clusters will be more skewed, because the variation in width is much smaller than in height for a person.

So the understanding we have to take is we have to think hard on how to scale a feature, because a wrong scale can have adverse effect on the cluster.

To identify the scale factor and to identify the clusters, we have to have the **Domain Knowledge.**

### [Domain Knowledge ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=422) ###

When we are involved in any type of learning be it supervised or unsupervised, the feature selection and scaling is critical, and to help in this regard we might need Domain Knowledge.

### [Minkowski metric ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=493) ###

Minkowski metric helps in doing the scaling, as per [wiki](http://en.wikipedia.org/wiki/Minkowski_distance)

> The Minkowski distance is a metric in a normed vector space which can be considered as a generalization of both the Euclidean distance and the Manhattan distance.

**Definition : ** 

The Minkowski distance of order p between two points

![](http://upload.wikimedia.org/math/1/1/e/11ed0dab51d86c81395e1def760c91c5.png)

is defined as

![](http://upload.wikimedia.org/math/a/a/0/aa0c62083c12390cb15ac3217de88e66.png)

For ![](http://upload.wikimedia.org/math/a/a/4/aa47fa19b67316cd180a645dec5bf0b7.png)  the Minkowski distance is a metric as a result of the Minkowski inequality.

Minkowski distance is typically used with p being 1 or 2. The latter is the Euclidean distance, while the former is sometimes known as the Manhattan distance.


As per wiki Manhattan distance is defined as:-

> The distance between two points in a grid based on a strictly horizontal and/or vertical path (that is, along the grid lines), as opposed to the diagonal or "as the crow flies" distance. The Manhattan distance is the simple sum of the horizontal and vertical components, whereas the diagonal distance might be computed by applying the Pythagorean theorem.

Till now we were dealing with feature vector which were comparable, i.e. they were mainly numbers, but a lot of time we have to deal with **Nominal category** of data, where we cannot use numbers to represent data.

In case of Nominal category of data, we convert these data to numbers with the help of Domain knowledge.

Once we have number representation of a **Nominal data**, we will use scaling or normalization, to generalize every feature between `0` and `1`. This is required because everything is normalized to the same dynamic range, and then we can compare them.

[Start Here.](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=866)

## K-Means Clustering : 41:25 ##





## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/lec20.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20_slides.pdf)
5. [Lecture data files (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/lec20_data.zip)

### Problem Sets ###

1. Problem Set 9: Schedule Optimization (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_ps9.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/ps9.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/ps9_sol.zip)
2. Problem Set 10 (Assigned)
    1. [Problem Set 10 Due on Lecture 22](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2)

### Check Yourself ###
### How do we use nominal (non-numeric or noncontinuous) categories as features? ###
### Why do we need to use scaling (normalization)? ###
### How does k-means clustering work? ###
