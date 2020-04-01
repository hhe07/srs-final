if __name__=='__main__':
    import multiprocessing as mp
    from stanfordcorenlp import StanfordCoreNLP
    import pickle
    import time
    import process
    import logging
    def posProcess(filename, lang, output,corenlpdir):
        log = logging.FileHandler(output + '-debug.log', mode = "w")
        log.setLevel("DEBUG")
        streamformatter = logging.Formatter(fmt='%(levelname)s:\t%(threadName)s:\t%(funcName)s:\t\t%(message)s', datefmt='%H:%M:%S')
        log.setFormatter(streamformatter)

        logger = logging.getLogger(output)
        logger.setLevel("DEBUG")

        logger.addHandler(log)
        try:
            logger.debug("lang %s" % lang)
            print("Running multi_trainer with lang %s" % lang)

            start = time.time()
            logger.debug("Start time %i" % start)
            
            postags = []
            jobs = []
            pool = mp.Pool(4)

            print("Opening file %s"% filename)
            f = pickle.load(open(filename, "rb"))
            
            x = [x for x in f]
            for y in x: 
                jobs.append(pool.apply_async(process.proc,[y],lang,corenlpdir))

            count = 0
            for job in jobs:
                while True:
                    time.sleep(1)
                    job.wait()
                    if job.successful():
                        tmp = ["*START*"]
                        tmp.extend(job.get())
                        postags.append(tmp)
                    count += 1
                    print("Sentences Processed: %i / %i , %f percent completed. \n" % (count,len(x),count/len(x)*100), end = "\033[F", flush = True)
                    break
            pickle.dump(postags, open(output,"wb"))
            print("Time Elapsed %i "% (time.time()-start))
            pool.close()

        except KeyboardInterrupt:
            print("Unsafe exiting, bye.")
            pass
        
    posProcess("sce_zh.xml.p","zh","zh.p", r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\stanford-corenlp-full-2018-10-05")
    

