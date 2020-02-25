
#!/usr/bin/env python3

import threading
import queue
import time

from concur.integrations.glfw import main
from concur.core import listen, tag, multi_orr, nothing
from concur.extra_widgets.frame import frame, Frame
from concur.extra_widgets.image import image, Image


def thread(c, q, quit_q, max_fps):
    t0 = 0
    try:
        for x in c:
            t1 = time.perf_counter()
            time.sleep(0)
            if t1 - t0 > 1/max_fps:
                try:
                    q.put_nowait(x)
                except queue.Full:
                    pass
                t0 = t1
    finally:
        quit_q.put(None)

def quick_plot_w(quit_q, q, x0):
    frame_st = Frame((-1, -1), (1, 1))
    content_gen = x0
    while True:
        events = yield from multi_orr([
            tag("Quit", listen(quit_q)),
            frame("Frame", frame_st, content_gen=content_gen),
            tag("Queue", listen(q)),
            ])
        for tag_, value in events:
            if tag_ == "Queue":
                content_gen = value
            elif tag_ == "Frame":
                frame_st = value
            elif tag_ == "Quit":
                return
        yield


def quick_plot(overlay_gen):
    q = queue.Queue(1)
    quit_q = queue.Queue(1)
    t = threading.Thread(target=thread, args=(overlay_gen, q, quit_q))

    t.start()
    x0 = q.get()
    main("Quick Plot", quick_plot_w(quit_q, q, x0), 500, 500)


def quick_window_w(quit_q, q, x0):
    st = nothing()
    while True:
        events = yield from multi_orr([
            tag("Quit", listen(quit_q)),
            st,
            tag("Queue", listen(q)),
            ])
        for tag_, value in events:
            if tag_ == "Queue":
                st = value
            elif tag_ == "Frame":
                frame_st = value
            elif tag_ == "Quit":
                return
        yield



def quick_window(widget_gen):
    q = queue.Queue(1)
    quit_q = queue.Queue(1)
    t = threading.Thread(target=thread, args=(widget_gen, q, quit_q))

    t.start()
    x0 = q.get()
    main("Quick Window", quick_window_w(quit_q, q, x0), 500, 500)


def quick_image_w(quit_q, q, x0):
    im_st = Image(x0[0]())
    content_gen = x0[1]
    while True:
        events = yield from multi_orr([
            tag("Quit", listen(quit_q)),
            image("Image", im_st, content_gen=content_gen),
            tag("Queue", listen(q)),
            ])
        for tag_, value in events:
            if tag_ == "Queue":
                content_gen = value[1]
                im_st.change_image(value[0]())
            elif tag_ == "Image":
                im_st = value
            elif tag_ == "Quit":
                return
        yield


def quick_image(overlay_gen, w, h, max_fps=60):
    q = queue.Queue(1)
    quit_q = queue.Queue(1)
    t = threading.Thread(target=thread, args=(overlay_gen, q, quit_q, max_fps))

    t.start()
    x0 = q.get()
    main("Quick Plot", quick_image_w(quit_q, q, x0), w, h)