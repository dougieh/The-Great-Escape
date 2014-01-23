#!/usr/bin/python
#
# Decode room data.
#
# dpt

obstr = [
    "interiorobject_TUNNEL_0",
    "interiorobject_SMALL_TUNNEL_ENTRANCE",
    "interiorobject_ROOM_OUTLINE_2",
    "interiorobject_TUNNEL_3",
    "interiorobject_TUNNEL_JOIN_4",
    "interiorobject_PRISONER_SAT_DOWN_MID_TABLE",
    "interiorobject_TUNNEL_CORNER_6",
    "interiorobject_TUNNEL_7",
    "interiorobject_WIDE_WINDOW",
    "interiorobject_EMPTY_BED",
    "interiorobject_SHORT_WARDROBE",
    "interiorobject_CHEST_OF_DRAWERS",
    "interiorobject_TUNNEL_12",
    "interiorobject_EMPTY_BENCH",
    "interiorobject_TUNNEL_14",
    "interiorobject_DOOR_FRAME_15",
    "interiorobject_DOOR_FRAME_16",
    "interiorobject_TUNNEL_17",
    "interiorobject_TUNNEL_18",
    "interiorobject_PRISONER_SAT_DOWN_END_TABLE",
    "interiorobject_COLLAPSED_TUNNEL",
    "interiorobject_ROOM_OUTLINE_21",
    "interiorobject_CHAIR_POINTING_BOTTOM_RIGHT",
    "interiorobject_OCCUPIED_BED",
    "interiorobject_WARDROBE_WITH_KNOCKERS",
    "interiorobject_CHAIR_POINTING_BOTTOM_LEFT",
    "interiorobject_CUPBOARD",
    "interiorobject_ROOM_OUTLINE_27",
    "interiorobject_TABLE_1",
    "interiorobject_TABLE_2",
    "interiorobject_STOVE_PIPE",
    "interiorobject_STUFF_31",
    "interiorobject_TALL_WARDROBE",
    "interiorobject_SMALL_SHELF",
    "interiorobject_SMALL_CRATE",
    "interiorobject_SMALL_WINDOW",
    "interiorobject_DOOR_FRAME_36",
    "interiorobject_NOTICEBOARD",
    "interiorobject_DOOR_FRAME_38",
    "interiorobject_DOOR_FRAME_39",
    "interiorobject_DOOR_FRAME_40",
    "interiorobject_ROOM_OUTLINE_41",
    "interiorobject_CUPBOARD_42",
    "interiorobject_MESS_BENCH",
    "interiorobject_MESS_TABLE",
    "interiorobject_MESS_BENCH_SHORT",
    "interiorobject_ROOM_OUTLINE_46",
    "interiorobject_ROOM_OUTLINE_47",
    "interiorobject_TINY_TABLE",
    "interiorobject_TINY_DRAWERS",
    "interiorobject_DRAWERS_50",
    "interiorobject_DESK",
    "interiorobject_SINK",
    "interiorobject_KEY_RACK"
]

roomdefs = [
    ["roomdef_1_hut1_right",0x6C15,[0x00,0x03,0x36,0x44,0x17,0x22,0x36,0x44,0x27,0x32,0x36,0x44,0x37,0x44,0x04,0x00,0x01,0x03,0x0A,0x0A,0x02,0x01,0x04,0x08,0x08,0x00,0x08,0x02,0x03,0x17,0x0A,0x05,0x17,0x06,0x07,0x0F,0x0F,0x08,0x18,0x12,0x05,0x18,0x14,0x06,0x09,0x02,0x09,0x10,0x07,0x0A]],
    ["roomdef_2_hut2_left",0x6C47,[0x01,0x02,0x30,0x40,0x2B,0x38,0x18,0x26,0x1A,0x28,0x02,0x0D,0x08,0x08,0x1B,0x03,0x06,0x08,0x06,0x02,0x28,0x10,0x05,0x1E,0x04,0x05,0x17,0x08,0x07,0x10,0x07,0x09,0x1D,0x0B,0x0C,0x01,0x05,0x09]],
    ["roomdef_3_hut2_right",0x6C6D,[0x00,0x03,0x36,0x44,0x17,0x22,0x36,0x44,0x27,0x32,0x36,0x44,0x37,0x44,0x04,0x00,0x01,0x03,0x0A,0x0A,0x02,0x01,0x04,0x08,0x08,0x00,0x08,0x02,0x03,0x17,0x0A,0x05,0x17,0x06,0x07,0x17,0x02,0x09,0x0B,0x10,0x05,0x0F,0x0F,0x08,0x0A,0x12,0x05,0x10,0x07,0x0A]],
    ["roomdef_4_hut3_left",0x6C9F,[0x01,0x02,0x18,0x28,0x18,0x2A,0x30,0x40,0x2B,0x38,0x03,0x12,0x14,0x08,0x09,0x1B,0x03,0x06,0x28,0x10,0x05,0x08,0x06,0x02,0x1E,0x04,0x05,0x09,0x08,0x07,0x10,0x07,0x09,0x16,0x0B,0x0B,0x19,0x0D,0x0A,0x1F,0x0E,0x0E]],
    ["roomdef_5_hut3_right",0x6CC9,[0x00,0x03,0x36,0x44,0x17,0x22,0x36,0x44,0x27,0x32,0x36,0x44,0x37,0x44,0x04,0x00,0x01,0x03,0x0A,0x0A,0x02,0x01,0x04,0x08,0x08,0x00,0x08,0x02,0x03,0x17,0x0A,0x05,0x17,0x06,0x07,0x17,0x02,0x09,0x0F,0x0F,0x08,0x0B,0x10,0x05,0x0B,0x14,0x07,0x10,0x07,0x0A]],
    ["roomdef_6_corridor",0x6CFB,[0x02,0x00,0x01,0x09,0x05,0x2E,0x03,0x06,0x26,0x0A,0x03,0x26,0x04,0x06,0x10,0x05,0x0A,0x0A,0x12,0x06]],
    ["roomdef_9_crate",0x6D0F,[0x01,0x01,0x3A,0x40,0x1C,0x2A,0x02,0x04,0x15,0x0A,0x1B,0x03,0x06,0x23,0x06,0x03,0x21,0x09,0x04,0x24,0x0C,0x06,0x0F,0x0D,0x0A,0x20,0x10,0x06,0x0A,0x12,0x08,0x1A,0x03,0x06,0x22,0x06,0x08,0x22,0x04,0x09]],
    ["roomdef_10_lockpick",0x6D37,[0x04,0x02,0x45,0x4B,0x20,0x36,0x24,0x2F,0x30,0x3C,0x03,0x06,0x0E,0x16,0x0E,0x2F,0x01,0x04,0x0F,0x0F,0x0A,0x23,0x04,0x01,0x35,0x02,0x03,0x35,0x07,0x02,0x20,0x0A,0x02,0x2A,0x0D,0x03,0x2A,0x0F,0x04,0x2A,0x11,0x05,0x1D,0x0E,0x08,0x0B,0x12,0x08,0x0B,0x14,0x09,0x22,0x06,0x05,0x1D,0x02,0x06]],
    ["roomdef_11_papers",0x6D70,[0x04,0x01,0x1B,0x2C,0x24,0x30,0x01,0x17,0x09,0x2F,0x01,0x04,0x21,0x06,0x03,0x20,0x0C,0x03,0x32,0x0A,0x03,0x0A,0x0E,0x05,0x26,0x02,0x02,0x32,0x12,0x07,0x32,0x14,0x08,0x33,0x0C,0x0A]],
    ["roomdef_12_corridor",0x6D94,[0x01,0x00,0x02,0x04,0x07,0x04,0x1B,0x03,0x06,0x23,0x06,0x03,0x10,0x09,0x0A,0x0F,0x0D,0x0A]],
    ["roomdef_13_corridor",0x6DA6,[0x01,0x00,0x02,0x04,0x08,0x06,0x1B,0x03,0x06,0x26,0x06,0x03,0x10,0x07,0x09,0x0F,0x0D,0x0A,0x32,0x0C,0x05,0x0B,0x0E,0x07]],
    ["roomdef_14_torch",0x6DBE,[0x00,0x03,0x36,0x44,0x16,0x20,0x3E,0x44,0x30,0x3A,0x36,0x44,0x36,0x44,0x01,0x01,0x09,0x02,0x01,0x04,0x26,0x04,0x03,0x31,0x08,0x05,0x09,0x0A,0x05,0x0B,0x10,0x05,0x0A,0x12,0x05,0x28,0x14,0x04,0x21,0x02,0x07,0x09,0x02,0x09]],
    ["roomdef_15_uniform",0x6DEA,[0x00,0x04,0x36,0x44,0x16,0x20,0x36,0x44,0x36,0x44,0x3E,0x44,0x28,0x3A,0x1E,0x28,0x38,0x43,0x04,0x01,0x05,0x0A,0x0F,0x0A,0x02,0x01,0x04,0x0A,0x10,0x04,0x09,0x0A,0x05,0x31,0x08,0x05,0x31,0x06,0x06,0x21,0x02,0x07,0x09,0x02,0x09,0x10,0x07,0x0A,0x0F,0x0D,0x09,0x1D,0x12,0x08]],
    ["roomdef_16_corridor",0x6E20,[0x01,0x00,0x02,0x04,0x07,0x04,0x1B,0x03,0x06,0x26,0x04,0x04,0x10,0x09,0x0A,0x0F,0x0D,0x0A]],
    ["roomdef_7_corridor",0x6E32,[0x01,0x00,0x01,0x04,0x04,0x1B,0x03,0x06,0x26,0x04,0x04,0x0F,0x0D,0x0A,0x20,0x0C,0x04]],
    ["roomdef_18_radio",0x6E43,[0x04,0x03,0x26,0x38,0x30,0x3C,0x26,0x2E,0x27,0x3C,0x16,0x20,0x30,0x3C,0x05,0x0B,0x11,0x10,0x18,0x19,0x0A,0x2F,0x01,0x04,0x1A,0x01,0x04,0x23,0x04,0x01,0x21,0x07,0x02,0x28,0x0A,0x01,0x1D,0x0C,0x07,0x2D,0x0C,0x09,0x1D,0x12,0x0A,0x30,0x10,0x0C,0x10,0x05,0x07]],
    ["roomdef_19_food",0x6E76,[0x01,0x01,0x34,0x40,0x2F,0x38,0x01,0x07,0x0B,0x1B,0x03,0x06,0x23,0x06,0x03,0x1A,0x09,0x03,0x2A,0x0C,0x03,0x2A,0x0E,0x04,0x1D,0x09,0x06,0x21,0x03,0x05,0x34,0x03,0x07,0x0B,0x0E,0x07,0x28,0x10,0x05,0x10,0x09,0x0A]],
    ["roomdef_20_redcross",0x6EA0,[0x01,0x02,0x3A,0x40,0x1A,0x2A,0x32,0x40,0x2E,0x36,0x02,0x15,0x04,0x0B,0x1B,0x03,0x06,0x0F,0x0D,0x0A,0x21,0x09,0x04,0x1A,0x03,0x06,0x22,0x06,0x08,0x22,0x04,0x09,0x1D,0x09,0x06,0x20,0x0E,0x05,0x20,0x10,0x06,0x18,0x12,0x08,0x30,0x0B,0x08]],
    ["roomdef_22_red_key",0x6ECF,[0x03,0x02,0x36,0x40,0x2E,0x38,0x3A,0x40,0x24,0x2C,0x02,0x0C,0x15,0x07,0x29,0x05,0x06,0x25,0x04,0x04,0x21,0x09,0x04,0x22,0x06,0x08,0x10,0x09,0x08,0x1D,0x09,0x06,0x28,0x0E,0x04]],
    ["roomdef_23_breakfast",0x6EF2,[0x00,0x01,0x36,0x44,0x22,0x44,0x02,0x0A,0x03,0x0C,0x02,0x01,0x04,0x23,0x08,0x00,0x23,0x02,0x03,0x10,0x07,0x0A,0x2C,0x05,0x04,0x2A,0x12,0x04,0x28,0x14,0x04,0x0F,0x0F,0x08,0x2B,0x07,0x06,0x0D,0x0C,0x05,0x0D,0x0A,0x06,0x0D,0x08,0x07]],
    ["roomdef_24_solitary",0x6F20,[0x03,0x01,0x30,0x36,0x26,0x2E,0x01,0x1A,0x03,0x29,0x05,0x06,0x28,0x0E,0x04,0x30,0x0A,0x09]],
    ["roomdef_25_breakfast",0x6F32,[0x00,0x01,0x36,0x44,0x22,0x44,0x00,0x0B,0x02,0x01,0x04,0x23,0x08,0x00,0x1A,0x05,0x03,0x23,0x02,0x03,0x28,0x12,0x03,0x2C,0x05,0x04,0x2B,0x07,0x06,0x0D,0x0C,0x05,0x0D,0x0A,0x06,0x0D,0x08,0x07,0x0D,0x0E,0x04]],
    ["roomdef_28_hut1_left",0x6F5B,[0x01,0x02,0x1C,0x28,0x1C,0x34,0x30,0x3F,0x2C,0x38,0x03,0x08,0x0D,0x13,0x08,0x1B,0x03,0x06,0x08,0x06,0x02,0x28,0x0E,0x04,0x1A,0x03,0x06,0x17,0x08,0x07,0x10,0x07,0x09,0x19,0x0F,0x0A,0x1D,0x0B,0x0C]],
    ["roomdef_29_second_tunnel_start",0x6F82,[0x05,0x00,0x06,0x1E,0x1F,0x20,0x21,0x22,0x23,0x06,0x00,0x14,0x00,0x00,0x10,0x02,0x00,0x0C,0x04,0x00,0x08,0x06,0x00,0x04,0x08,0x00,0x00,0x0A]],
    ["roomdef_31",0x6F9E,[0x06,0x00,0x06,0x24,0x25,0x26,0x27,0x28,0x29,0x06,0x03,0x00,0x00,0x03,0x04,0x02,0x03,0x08,0x04,0x03,0x0C,0x06,0x03,0x10,0x08,0x03,0x14,0x0A]],
    ["roomdef_36",0x6FBA,[0x07,0x00,0x06,0x1F,0x20,0x21,0x22,0x23,0x2D,0x05,0x00,0x14,0x00,0x00,0x10,0x02,0x00,0x0C,0x04,0x00,0x08,0x06,0x0E,0x04,0x08]],
    ["roomdef_32",0x6FD3,[0x08,0x00,0x06,0x24,0x25,0x26,0x27,0x28,0x2A,0x05,0x03,0x00,0x00,0x03,0x04,0x02,0x03,0x08,0x04,0x03,0x0C,0x06,0x11,0x10,0x08]],
    ["roomdef_34",0x6FEC,[0x06,0x00,0x06,0x24,0x25,0x26,0x27,0x28,0x2E,0x06,0x03,0x00,0x00,0x03,0x04,0x02,0x03,0x08,0x04,0x03,0x0C,0x06,0x03,0x10,0x08,0x12,0x14,0x0A]],
    ["roomdef_35",0x7008,[0x06,0x00,0x06,0x24,0x25,0x26,0x27,0x28,0x29,0x06,0x03,0x00,0x00,0x03,0x04,0x02,0x04,0x08,0x04,0x03,0x0C,0x06,0x03,0x10,0x08,0x03,0x14,0x0A]],
    ["roomdef_30",0x7024,[0x05,0x00,0x07,0x1E,0x1F,0x20,0x21,0x22,0x23,0x2C,0x06,0x00,0x14,0x00,0x00,0x10,0x02,0x00,0x0C,0x04,0x06,0x08,0x06,0x00,0x04,0x08,0x00,0x00,0x0A]],
    ["roomdef_40",0x7041,[0x09,0x00,0x06,0x1E,0x1F,0x20,0x21,0x22,0x2B,0x06,0x07,0x14,0x00,0x00,0x10,0x02,0x00,0x0C,0x04,0x00,0x08,0x06,0x00,0x04,0x08,0x00,0x00,0x0A]],
    ["roomdef_44",0x705D,[0x08,0x00,0x05,0x24,0x25,0x26,0x27,0x28,0x05,0x03,0x00,0x00,0x03,0x04,0x02,0x03,0x08,0x04,0x03,0x0C,0x06,0x0C,0x10,0x08]],
    ["roomdef_50_blocked_tunnel",0x7075,[0x05,0x01,0x34,0x3A,0x20,0x36,0x06,0x1E,0x1F,0x20,0x21,0x22,0x2B,0x06,0x07,0x14,0x00,0x00,0x10,0x02,0x00,0x0C,0x04,0x14,0x08,0x06,0x00,0x04,0x08,0x00,0x00,0x0A]],
]

notes = {
    0x6C61: "player's bed",
    0x6C89: "bed_A",
    0x6C8A: "bed_C",
    0x6C8D: "bed_B",
    0x6CE6: "bed_D",
    0x6CE9: "bed_E",
    0x6CEC: "bed_F",
    0x6F17: "bench_A",
    0x6F4F: "bench_D",
    0x708C: "collapsed_tunnel_obj",
}

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

for room in roomdefs:
    name, base, roomdef = room[0], room[1], room[2]
    #print name, base, roomdef

    output = []
    output.append("D $%X %s" % (base, name))

    i = 0

    output.append("  $%X,1 %d" % (base + i, roomdef[i]))
    i += 1

    nboundaries = roomdef[i]
    output.append("  $%X,1 %d /* count of boundaries */" % (base + i, roomdef[i]))
    i += 1
    for n in range(nboundaries):
        output.append("  $%X,4 { %d, %d, %d, %d }, /* boundary */" % (base + i, roomdef[i], roomdef[i + 1], roomdef[i + 2], roomdef[i + 3]))
        i += 4

    ntbd = roomdef[i]
    output.append("  $%X,1 %d /* count of TBD */" % (base + i, roomdef[i]))
    i += 1
    output.append("  $%X,%d %s /* data TBD */" % (base + i, ntbd,
        str(roomdef[i:i+ntbd])))
    i += ntbd

    nobjs = roomdef[i]
    output.append("  $%X,1 %d /* count of objects */" % (base + i, roomdef[i]))
    i += 1
    for n in range(nobjs):
        ob, x, y = roomdef[i:i+3]
        padding = " " * (42 - len(obstr[ob]))
        addr = base + i
        if addr in notes:
            comment = " /* %s */" % notes[addr]
        else:
            comment = ""
        output.append("  $%X,3 { %s,%s%2d, %2d },%s" % (addr, obstr[ob], padding, x, y, comment))
        i += 3

    print '\n'.join(output)

    print

