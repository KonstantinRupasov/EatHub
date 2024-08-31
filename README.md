# EatHub
Agile Recipe Development and Production

- Developing a food recipe is an iterative process that includes a lot of tries and errors. There seems to be no app aimed at automating it:
    - Please point me into the direction of this kind of apps out there if you seen any
- During my home cook "career" I developed dozens of recipes and always thought I could benefit from some kind of Agile automation.
- This repository is my first attempt to create a prototype of such an app

Main focus of the app:

- JSON-based language allowing to define the recipe
- Git-based version control
- Virtual agile "pipeline" for recipes:
  - Versions
  - Releases
  - Release types:
    - Prototype
    - Candidate
    - Prod
    - etc.
- Interactive engine that "runs" recipes:
  - Guides you through the recipe step by step
  - Gives you instructions of what to do on each step
  - Allows to run several independent threads for a single recipe (if you have several cooks working at the same time)
  - Allows to run multiple recipes at the same time
  - Automatically spreads the workload between your team members

Use cases:

- Test kitchen or a restaurant developing a recipe
- Restaurant, running multiple concurrent preparations at the same time
