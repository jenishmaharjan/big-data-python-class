from mrjob.job import MRJob
from mrjob.step import MRStep

class CountOrderlessTrigrams(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.top10)
        ]
    
    """ Here the key will be a list of 3 words instead of 2. And the sorted() method is used to disregard the order of these words."""
    def mapper(self, _, line): 
        line = line.lower().split()           
        for words in zip(line, line[1:], line[2:]):
            yield list(sorted((words[0], words[1], words[2]))), 1 
           
    def combiner(self, trigram, counts):
        yield trigram, sum(counts)                
                               
    def reducer(self, trigram, counts):          
        yield None, (trigram, sum(counts))
                   
    def top10(self, _, trigram_count):
        for i in sorted(trigram_count, key=lambda x:x[1], reverse=True)[:10]:
                   yield i

            
if __name__ == '__main__':
    CountOrderlessTrigrams.run()