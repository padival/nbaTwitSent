var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('mydb.db');

db.serialize(function() {
	//Creates tables if not already made
	db.run("CREATE TABLE if not exists tweets (score INTEGER, hashtag TEXT, author TEXT, date TEXT, tweet_text TEXT)");
	db.run("CREATE TABLE if not exists team (score INTEGER, total_tweets INTEGER, standing INTEGER, team_name TEXT)");
	
	//Add to table prepare statement
	var stmt = db.prepare("INSERT INTO team VALUES (?, ?, ?, ?)");
	//Insert variables and finalize
	stmt.run(50, 4000, 1, "Lakers");
	stmt.finalize();

	//Output to console
	db.each("SELECT team_name, standing, score, total_tweets FROM team", function(err, row) {
		console.log('Team: ' + row.team_name + " total_tweets: " + row.total_tweets + " Score: " + row.score + " Standing: " + row.standing);
	});
});
//Close DB
db.close();