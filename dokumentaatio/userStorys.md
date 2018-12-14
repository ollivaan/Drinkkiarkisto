# UserStorys

* As a user i can add new drinks to the database so that i can create drinks
`INSERT INTO drink (name) VALUES ('<name>');`
* As a user i can add new ingredient to the database so that i can create new drink recipies
`INSERT INTO ingredient (name) VALUES ('<name>');`
* As a user i can view all the drinks in the database
`SELECT * FROM drink;`
* As a user i can view all the ingredients in the database
`SELECT * FROM ingredient;`
* As a user i can edit ingredients in the database
`UPDATE ingredient SET name = '<new name>';`
* As a user i can edit drinks in the database
`UPDATE drink SET name = '<new name>';`
* As a user i can delete ingredients in the database
`DELETE FROM drink WHERE drink.id = '<id>';`
* As a user i can delete drinks in the database
`DELETE FROM drink WHERE drink.id = '<id>';`
