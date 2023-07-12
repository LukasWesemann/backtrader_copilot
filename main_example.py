from bt_copilot import BtCopilot
from coding_agent import SimpleCodingAgent
from dotenv import load_dotenv
import os

'''
--------------------------------------------------------------------------
--> Setup
--> All directories and settings kept as defaults
--------------------------------------------------------------------------
'''

# Load environment variables
# place .env file in root directory
# content .env file: API_KEY="your_OpenAI_API_key"
# IMPORTANT: set a usage limit on your OpenAI account to avoid unintentionally high API costs

load_dotenv()

# Initialise coding agent
coding_agent = SimpleCodingAgent(API_KEY = os.getenv("API_KEY"),
                                 test_mode = False)

# Initialise copilot client
copilot = BtCopilot(coding_agent = coding_agent)

'''
--------------------------------------------------------------------------
--> Load existing backtesting code to describe and visualise the strategy
--------------------------------------------------------------------------
'''

copilot.load_code('resources/example_backtest.py')


# Describe strategy in natural language
generated_description = copilot.get_strategy_description()
print(generated_description)

# Visualise strategy based on stored backtrader code
# IMPORTANT: Requires graphviz to be installed on your system
# copilot.visualise_strategy(vis_basis = 'code')

copilot.prompt_elements['strategy'] = generated_description
copilot.visualise_strategy(vis_basis = 'description')

'''
--------------------------------------------------------------------------
--> Get natural language feedback for improvements based on existing strategy
--------------------------------------------------------------------------
'''

# Based on loaded backtesting code
feedback_from_code = copilot.get_strategy_feedback(feedback_basis = 'code')
print(feedback_from_code)

# Based on natural language description of strategy rules
feedback_from_description = copilot.get_strategy_feedback(feedback_basis = 'description')
print(feedback_from_description)

'''
--------------------------------------------------------------------------
--> Build backtest from natural language input
--------------------------------------------------------------------------
'''

# Add data for the backtest to be executed on
data_description = '''
Use btc-usd.csv that I downloaded from yahoo finance. Load only from May 2022 to March 2023.
'''
copilot.set_datapipeline(user_input = data_description)

# Add trading strategy rules
strategy_description = '''
'Use two moving averages 7 and 13 days. When we are not in a position and 
7 crosses above 13 go long, close wenn 7 crosses below 13. Also close if stop-loss 15% is hit.'
'''
copilot.set_strategy(user_input = strategy_description)

# Add analysers
analysers_description = '''
Use the total PNL and the sharpe ratio and print them out when the backtest is finished.
'''
copilot.set_analysers(user_input = analysers_description)

# Compose full prompt to be executed by
copilot.compose_prompt_from_elements()

# Build code based on composed prompt
copilot.build_code_from_prompt()

# Save code to file (uses default directory '/outputs' and default project name 'myBacktest' for filename)
copilot.save_code()

# Execute backtest
# copilot.run_backtest()

