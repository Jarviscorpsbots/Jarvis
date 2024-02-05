import math

import pynewtonmath as newton
from telegram import Update
from telegram.ext import CallbackContext

from jarvis import dispatcher
from jarvis.modules.disable import DisableAbleCommandHandler


def simplify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.simplify("{}".format(args[0])))


def factor(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.factor("{}".format(args[0])))


def derive(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.derive("{}".format(args[0])))


def integrate(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.integrate("{}".format(args[0])))


def zeroes(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.zeroes("{}".format(args[0])))


def tangent(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.tangent("{}".format(args[0])))


def area(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.area("{}".format(args[0])))


def cos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))


def sin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))


def tan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))


def arccos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))


def arcsin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))


def arctan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))


def abs(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))


def log(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))


__help__ = """
*MATHS*
Solves complex math problems using https://newton.now.sh
❍ /math*:* Math `/math 2^2+2(2)`
❍ /factor*:* Factor `/factor x^2 + 2x`
❍ /derive*:* Derive `/derive x^2+2x`
❍ /integrate*:* Integrate `/integrate x^2+2x`
❍ /zeroes*:* Find 0's `/zeroes x^2+2x`
❍ /tangent*:* Find Tangent `/tangent 2lx^3`
❍ /area*:* Area Under Curve `/area 2:4lx^3`
❍ /cos*:* Cosine `/cos pi`
❍ /sin*:* Sine `/sin 0`
❍ /tan*:* Tangent `/tan 0`
❍ /arccos*:* Inverse Cosine `/arccos 1`
❍ /arcsin*:* Inverse Sine `/arcsin 0`
❍ /arctan*:* Inverse Tangent `/arctan 0`
❍ /abs*:* Absolute Value `/abs -1`
❍ /log*:* Logarithm `/log 2l8`

_Keep in mind_: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""

__mod_name__ = "Mᴀᴛʜs"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("math", simplify, run_async=True)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor, run_async=True)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", derive, run_async=True)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate, run_async=True)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes, run_async=True)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent, run_async=True)
AREA_HANDLER = DisableAbleCommandHandler("area", area, run_async=True)
COS_HANDLER = DisableAbleCommandHandler("cos", cos, run_async=True)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin, run_async=True)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan, run_async=True)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos, run_async=True)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin, run_async=True)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan, run_async=True)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs, run_async=True)
LOG_HANDLER = DisableAbleCommandHandler("log", log, run_async=True)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER)
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)
