# C - Hash tables
## What is a hash function
* A hash function is a fundamental concept in hash tables. It's a mathematical function that takes an input (or "key") and produces a fixed-size string of characters, which is typically a numerical value. The output of a hash function is often referred to as a "hash code".
## What Makes a Good Hash Function?
### To ensure that a hash function works efficiently and minimize collision, it should posses the following:
* Fast computation: Hash functions should be computationally efficient. They should generate hash codes quickly, as one of the main benefits of using hash tables is their speed.
* Uniform Distribution: It should evenly distribute keys across the range of hash codes. Helps in minimizing collisions, which occur when two different keys produce the same hash code. A non-uniform distribution can lead to performance issues, as some buckets in the hash table may become significantly overloaded.
* Avalanche Effect: A small change in the input should result in a drastically different hash code. This property ensures that similar keys don't collide frequently.
* Independence of Input Size: The quality of the hash code should not depend on the size of the input key. A good hash function should be able to hash keys of different lengths effectively.
## 