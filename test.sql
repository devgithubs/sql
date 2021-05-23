select count(*) from Track;
select count(*) from Artist;

SELECT COUNT(FirstName) 
FROM Customer 
WHERE Employee.LastName = 'Peacock' AND Employee.FirstName = 'Jane';