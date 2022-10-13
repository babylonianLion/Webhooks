// Author: Hussain Al Zerjawi
// Purpose: Practicing webhooks using JavaScript/NodeJS
// Date: 12/10/2022

// This webhook uses the FETCH API that is still an experimental feature within NodeJS

// Destination URL to which the webhook should send the POST request when an event occurs.
let url = "https://webhook.site/03c00641-845b-479e-bd67-e33d0a408485"

// The payload/data that is being sent.
let data = {
    name: 'Mr JavaScript Tester',
    company: 'Ooredoo'
  };
  
// Using the FETCH API the data is sent as a POST request.
// However, before being sent the data object is converted into a JSON
  let response = fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  });
  
  let result = response;
  console.log(result.message);