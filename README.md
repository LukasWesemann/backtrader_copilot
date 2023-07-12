# backtrader_copilot v0.1.0

### Goal

The goal of *backtrader_copilot* is to leverage the power of AI to make powerful quantitative backtesting more efficient for professionals, as well as making it available to amateurs who have great ideas but lack the technical skills to test them.

Using *backtrader_copilot* allows users to interact with a complex backtesting framework via natural language. Although not achievied in this  version, the big picture goal is to remove the requirement for deep understanding of the code base on the user side and allow them to focus on creativity, strategic decision making and planning.

I aim to achieve this by providing useful features revolving around extracting natural language descriptions of implemented backtests, generating visual flow charts of backtesting architecture and trading strategies based on code or descirptions, providing natural language feedback and suggestions for trading strategies and datasets, and generating backtesting code based on natural language descriptions provided by the user.

## Introduction

*backtrader_copilot* is an AI enabled no-code tool to conduct quantitative backtests for trading strategies.

backtrader is a popular python framework that enables algorithmic traders to backtest complex trading strategies on historical data.

Setting up quantitative backtests is a complex task that involves data selection and cleaning, strategy ideation, backtest implementation, strategy optimisation and evaluation of KPI's.

Backtrader is an excellent tool to support this. However, I see several limitations

- It's quite complex to set up backtests. Many concepts are not intuitively clear to beginners and there are many pitfalls.
- Quantiative backtesting is computationally intense. Writing efficient code is crucial, but how to achieve this is not always obvious.
- The speed at which trading strategy ideas can be translated into code is low.
- It is hard to get feedback on trading stragies and developing new ideas based on existing strategies can be cumbersome.

*backtrader_copilot* leverages large language models (LLM's) to:

- set up backtesting code according to natural language descriptions provided by the user
- identifies issues with provided strategies
- provides suggestions for improvements of strategies and data sources
- provides an intuitive UI for non-technical traders to use *backtrader_copilot*

Here only the OpenAI API is implemented via LangChain. Future iterations will have endpoints for different LLM's available.
### Features

- Loading backtrader code
- Generating natural language descriptions of implemented strategy rules
- Generating a graph visualisation of the implemented backtest (required graphviz installed)
- Generating feedback for implemented trading strategy
- Generating backtrader backtest code based on natural language description for 
  - data
  - strategies
  - analysers
  - (...) more to come
- Autopilot that guides user through the process of setting up a backtest in backtrader by asking a series of questions.
- Save generated code

## Quick start guide

- see *main_example.py*  

### Limitations

 - A lot of limitations, this is v0.1 with the aim of providing functioning basic infrastructure.
 - This version can only provide very limited and simple but functioning examples, this version is not production ready.
 - Simple prompt templates are implemented, these have a lot of potential for improvement.
 - No web-based UI yest (planned).
 - No custom indicators yet (planned).
 - Only a single shot implementation of the coding agent. More complex code implementation and testing strategies will be required (planned).
 - Autopilot is static and does not ask dynamic questions yet (planned)
 - No logging implemented (planned).