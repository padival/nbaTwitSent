// Server backend script
// This script includes the app routing for other pages
// we would like to serve.

// Dependencies
var express = require("express");

//Require statements
var sqlite3 = require("sqlite3").verbose();
var db = new sqlite3.Database('db.db');

var app = express();

//Database function
db.serialize(function() {
	//Creates tables if they do not yet exist
	db.run("CREATE TABLE if not exists tweets (score INTEGER, hashtag TEXT, author TEXT, date TEXT, tweet_text TEXT)");
	db.run("CREATE TABLE if not exists team (name TEXT, score INTEGER, total_tweets INTEGER, standing INTEGER)");
	
	//Insert statement in the form of prepare->run->finalize
	var stmt = db.prepare("INSERT INTO team VALUES (?, ?, ?, ?)");
	stmt.run("Lakers", 45, 5000, 19);
	stmt.finalize();

	//Output to console
	db.each("SELECT name, score, total_tweets, standing FROM team", function(err, row) {
		console.log('Team: ' + row.name + " Score: " + row.score + " total_tweets: " + row.total_tweets + " Standing: " + row.standing);
	});
});
//Close DB
db.close();	


// Index page route
app.get('/', function (req, res) {
    res.sendFile('index.html', { root : '../public/model/' });  // setting the root dir will have express

});                                                             // start looking for the file in that particular dir

app.listen(5000);
console.log('Server is listening')