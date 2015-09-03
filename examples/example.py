from logsimple import logger

# normal print
logger.log('Hello World')											

# in red
logger.log('Hello World', color='r')								

# in red and bolded
logger.log('Hello World', color='r', format='b')					

# in red, bolded, and highlighted in yellow
logger.log('Hello World', color='r', format='b', highlight='y')		