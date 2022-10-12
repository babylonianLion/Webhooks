// This webhook uses the FETCH API that is still an experimental feature within NodeJS

let url = "https://webhook.site/03c00641-845b-479e-bd67-e33d0a408485"

let data = {
    name: 'Mr JavaScript Tester',
    company: 'Ooredoo'
  };
  
  let response = fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  });
  
  let result = response;
  console.log(result.message);