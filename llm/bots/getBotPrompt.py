import importlib.util
import sys

def get_prompt_from_file(file_path):
    try:
        # Get the full path and extract the module name
        module_name = file_path.split('/')[-1].split('.')[0]
        
        # Load the module specification
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            raise ImportError(f"Could not find the file: {file_path}")
        
        # Create the module
        module = importlib.util.module_from_spec(spec)
        
        # Add the module to sys.modules
        sys.modules[module_name] = module
        
        # Execute the module
        spec.loader.exec_module(module)
        
        # Get the prompt variable from the module
        if hasattr(module, 'prompt'):
            return module.prompt
        else:
            raise AttributeError(f"No 'prompt' variable found in {file_path}")
    
    except ImportError as e:
        print(str(e))
    except AttributeError as e:
        print(str(e))
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {str(e)}")
    
    return None

def getBotPrompt(botName):
    file_path = f"llm/bots/prompts/{botName}.py"
    botBasePrompt = get_prompt_from_file(file_path)
    if botBasePrompt is not None:
        return botBasePrompt;
    
