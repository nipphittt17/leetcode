# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete a from Person a LEFT join Person b ON a.email = b.email and a.id > b.id WHERE b.email is not NULL


