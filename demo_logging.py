import logging

file_name = 'logger.txt'
formatter = '%(asctime)s -- %(filename)s[line:%(lineno)d] %(levelname)s\t%(message)s'
logging.basicConfig(format = formatter, level = logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug('debug10')
logger.info('info20')
logger.warning('warning30')
logger.error('error40')
logger.critical('critical50')