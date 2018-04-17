from uuid import uuid4
from copy import deepcopy
from .board_constants import INITIAL_BOARD
import requests


PORT = 8080
API_URL = 'http://localhost:{}'.format(PORT)


class BaseBoard:
    GAMES = {}

    @classmethod
    def get_game(cls, _id):
        """
        Provide game matching id.
        """
        return cls.GAMES[_id]

    def __init__(self, _id, board=None):
        if _id:
            self.id = _id
        else:
            self.id = str(uuid4())
        self.GAMES[self.id] = self
        if board:
            self.board = board
        else:
            self.board = deepcopy(INITIAL_BOARD)

    def close(self):
        del self.GAMES[self.id]

    def current_state_v1(self):
        """
        Provide REST view of game state.
        """
        return {'board': self.board}

    def poke_player(self, end, active_player=None):
        """
        Inform active player of game state.
        """
        self.executor.submit(
            requests.put,
            f'{ API_URL }/agent/{ active_player or self.active_player() }',
            data={'end': False}
        ).add_done_callback(self.handle_future)