// Author: Hussain Al Zerjawi
// Purpose: Practicing webhooks using JavaScript/NodeJS
// Date: 12/10/2022

// Require express and body-parser
const express = require("express")
const bodyParser = require("body-parser")

// Initialize express and define a port
const app = express()
const PORT = 5000

// Tell express to use body-parser's JSON parsing
app.use(bodyParser.json())

// Start express on the defined Port
app.listen(PORT, () => console.log(`Server running on port ${PORT}`))

// app.use(bodyParser.json())
app.post("/webhook", (req, res) => {
    console.log(req.body) // Call your action on the request here
    res.status(200).end() // Responding with a 200 aka status OK
})
