from mrjob.job import MRJob
from mrjob.step import MRStep

class CountMonograms(MRJob):
 
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.top10)
        ]
    
    def mapper(self, _, line): 
        line = line.lower().split()           
        for words in zip(line, line[1:]):        
            yield words[0], 1 
   
    def combiner(self, monogram, counts):
        yield monogram, sum(counts)                
  
    def reducer(self, monogram, counts):          
        yield None, (monogram, sum(counts))
                   
    def top10(self, _, monogram_count):
        for i in sorted(monogram_count, key=lambda x:x[1], reverse=True)[:10]:
                   yield i

            
if __name__ == '__main__':
    CountMonograms.run()