from mrjob.job import MRJob
from mrjob.step import MRStep

class CountBigrams(MRJob):
    
    """ The steps() method basically is used to define the steps of the Map Reduce job being defined in the class"""
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.top10)
        ]
    
    """ The mapper() method takes a key and a value as args - Use of the character _ infers key is ignored
        The method changes the text to lowercase and then splits the text into words, default separator is whitespace.
        Finally the method yields list of key-value pairs. Here the key is the word pair, and the value is 1. """
    def mapper(self, _, line): 
        line = line.lower().split()           
        for words in zip(line, line[1:]):        
            yield list((words[0], words[1])), 1
            
    """ The combiner() method takes two word pairs as key and 1 as the value. 
        The method then yields the sum of 1s for recurring word pairs 
        Thus this method gives us the count of each existing word pair. """
    def combiner(self, bigram, counts):
        yield bigram, sum(counts)                
                               
    """ The reduce() method takes a key and an iterator of vaues.
        The method also yields key-value pairs"""
    def reducer(self, bigram, counts):          
        yield None, (bigram, sum(counts))
                   
    """ The top10() method sorts the word pair list on the basis of frequencey and yields the top 10 word pairs/bigrams"""
    def top10(self, _, bigram_count):
        for i in sorted(bigram_count, key=lambda x:x[1], reverse=True)[:10]:
                   yield i

            
if __name__ == '__main__':
    CountBigrams.run()