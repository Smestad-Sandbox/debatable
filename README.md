# Debatable

Debatable is a Python library that supplies a debate template. It provides a command-line interface (CLI) that takes two arguments: the API endpoint for first_debater and the API endpoint for second_debater. The CLI allows students to practice developing an API with the following endpoints: debater, opening_statement, cross_examination, rebuttal, final_focus, and conclusion.

##Installation
To install debatable, you can clone the repository:
```
git clone git@github.com:Smestad-Sandbox/debatable.git
```

##Usage
To use the Debate Template Library, you can run the following command:

```
debate-template --first_debater <first_debater_endpoint> --second_debator <second_debator_endpoint> --topic <topic>
```

The --first_debater and --second_debator arguments are required and should be the API endpoints for first_debater and second_debator, respectively. The --topic argument is optional and can be used to specify a topic for the debate.

Here's an example command:

```
debate --first_debater https://first_debater-api.com --second_debator https://second_debator-api.com --topic minecraft
```

##Endpoints
Debatable requires students create APIs with the following endpoints:

/debater
Returns a JSON object with two keys, name and introduction, that introduce the debater.

/opening_statement
Returns a JSON object with a response key that contains the opening statement for the debater.

/cross_examination
Returns a JSON object with a response key that contains the cross-examination for the debater.

/rebuttal
Returns a JSON object with a response key that contains the rebuttal for the debater.

/final_focus
Returns a JSON object with a response key that contains the final focus for the debater.

/conclusion
Returns a JSON object with a response key that contains the conclusion for the debater.

##Examples
Here are some example responses from the endpoints:

###debater
```
{
    "name": "John Smith",
    "introduction": "John Smith is a passionate advocate for..."
}
```

###opening_statement
```
{
    "response": "I believe that CSS is the most important..."
}
```

###cross_examination
```
{
    "response": "How can you say that CSS is more important than..."
}
```

###rebuttal
```
{
    "response": "I disagree with your argument because..."
}
```

###final_focus
```
{
    "response": "In conclusion, CSS is the most important..."
}
```

###conclusion
```
{
    "response": "Thank you for considering my argument..."
}
```

##License
The Debate Template Library is released under the AGPL License. See the LICENSE file for more information.
