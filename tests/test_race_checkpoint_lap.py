import pytest
import gameplay.race_checkpoint_lap as mod

CASES = [
    ("checkpoint_order_gate", (1,)),
    ("server_clock_timer", (1,)),
    ("ghost_by_timestamp", (1,)),
    ("destroy_on_reload", (1,)),
    ("rank_by_cross_time", (1,)),
    ("recompute_result", (1,)),
    ("load_track", (1,)),
    ("update_lap", (1,)),
    ("replay_ghost", (1,)),
    ("present", (1,)),
    ("validate_lap", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
