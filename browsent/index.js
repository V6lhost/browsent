const express = require("express");
const app = express()

var files = [
  {id: 0, name: "test.zip", size: "15MB", auth: false, thumbnail: "file.png"},
  {id: 1, name: "test.apk", size: "17MB", auth: false, thumbnail: "file.png"},
  {id: 2, name: "test.jpeg", size: "3MB", auth: true, thumbnail: "file-auth.png"},
  {id: 3, name: "test.doc", size: "10MB", auth: true, thumbnail: "file-auth.png"}
];

app.set("view engine", "ejs");

app.use(express.static('public'));
app.use(express.static('node_modules'));

app.use("/file/:name", function(req, res) {
  const file = files.find(f => f.name == req.params.name);
  if (!file) {
    res.send("file not found or unaccessible");
  } else {
   res.render("file", file);
  }
});

app.use("/files", function(req, res) {
  res.render("files", {
    files: files
  });
});

app.use("/404", function(req, res) {
  res.send("404 not found")
});

app.use("/", function(req, res) {
  res.render("index");
});

app.listen(3000, () => {
  console.log("listening on port 3000 started. link: http://localhost:3000/")
});