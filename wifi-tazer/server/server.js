var web = require("webstuff");
var app = web({
	port: 8099,
	host: "0.0.0.0"
});

app.static("web");

var tazing = false;

app.get("/await", (req, res) => {
	res.end(tazing ? "taze\n" : "");
});

app.post("/taze", (req, res) => {
	console.log("lol", new Date());
	tazing = true;
	setTimeout(() => tazing = false, 1000);
});
