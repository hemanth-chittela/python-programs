import logging

def cat():
    a=1
    b=2

    logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s",datefmt="%Y-%m-%d %H:%M:%S",filename="basic.log")
    sum=a+b
    logging.debug("this is a debug")
    logging.debug("this is a config")
    logging.critical("this is critical")
    logging.error("this is an error")
    logging.info("the answer is "+str(sum))

if __name__=="__main__":
    cat()
