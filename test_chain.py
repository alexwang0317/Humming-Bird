from NLP.chain import chain


def test_chain():
    print(
        chain.invoke({"text":"Hi, could you write me some code to make my drone arm, takeoff, land, and then disarm?"}).content
    )

# Seems like we're gonna need to provide other information, like serial port, baud rate, and have that stuff all saved beforehand? 
# Maybe have that be part of the prompt. 


test_chain()
