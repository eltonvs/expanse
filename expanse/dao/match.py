from abc import ABCMeta

from ..models.match import Match
from .generic import GenericDAO

class MatchDAO(GenericDAO):
	__metaclass__ = ABCMeta


class MatchDAOMongo(MatchDAO):

	__shered_state = {}

	def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, match):
    	match_to_insert = {
    		"teams": match.teams,
    		"score": match.score
    	}
    	self.db.matches.insert(match_to_insert)

    	return{}

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, query, update):
        print(query, update, self.db.matches.update(query, update))

    def get(self, query):
    	matches = list(self.db.matches.find(query))
    	if matches:
    		match_list = []
    		for match in matches:
    			new_match = Match(
    				match['teams'][0],
    				match['teams'][1])
    			new_match.score = match['score']
    			new_match.my_id = match['_id']
    			match_list.append(new_match)
    		return match_list

    def get_one(self, query):
    	matches = list(self.db.matches.find(query))
    	if matches:
    		new_match = Match(
    			match['teams'][0],
    			match['teams'][1])
    		new_match.score = match['score']
    		new_match.my_id = match['_id']
    		return new_match

    def list(self):
   		return self.get({})


