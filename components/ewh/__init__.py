import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch, text_sensor, time, uart
from esphome.const import (
    CONF_ENTITY_CATEGORY,
    CONF_ICON,
    CONF_ID,
    CONF_TIME_ID,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_TIMER,
)

CODEOWNERS = ["@dentra"]
AUTO_LOAD = ["switch", "text_sensor"]

CONF_BST = "bst"
CONF_CLOCK = "clock"
CONF_TIMER = "timer"

ICON_WATER_BOILER = "mdi:water-boiler"
ICON_CLOCK = "mdi:clock"

ewh_ns = cg.esphome_ns.namespace("ewh")

EWHComponent = ewh_ns.class_("EWHComponent", cg.Component, uart.UARTDevice)
BSTSwitch = EWHComponent.class_("BSTSwitch")


EWH_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_TIME_ID): cv.use_id(time.RealTimeClock),
            cv.Optional(CONF_ICON, default=ICON_WATER_BOILER): switch.icon,
            cv.Optional(CONF_BST): switch.SWITCH_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(BSTSwitch),
                    cv.Optional(
                        CONF_ENTITY_CATEGORY, default=ENTITY_CATEGORY_CONFIG
                    ): cv.entity_category,
                }
            ),
            cv.Optional(CONF_CLOCK): text_sensor.TEXT_SENSOR_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                    cv.Optional(CONF_ICON, default=ICON_CLOCK): switch.icon,
                    cv.Optional(
                        CONF_ENTITY_CATEGORY, default=ENTITY_CATEGORY_DIAGNOSTIC
                    ): cv.entity_category,
                }
            ),
            cv.Optional(CONF_TIMER): text_sensor.TEXT_SENSOR_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                    cv.Optional(CONF_ICON, default=ICON_TIMER): switch.icon,
                    cv.Optional(
                        CONF_ENTITY_CATEGORY, default=ENTITY_CATEGORY_DIAGNOSTIC
                    ): cv.entity_category,
                }
            ),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def new_ewh(config):
    urt = await cg.get_variable(config[uart.CONF_UART_ID])
    var = cg.new_Pvariable(config[CONF_ID], urt)
    await cg.register_component(var, config)

    if CONF_BST in config:
        conf = config[CONF_BST]
        sens = cg.new_Pvariable(conf[CONF_ID], var)
        await switch.register_switch(sens, conf)
        cg.add(var.set_bst(sens))

    if CONF_CLOCK in config:
        conf = config[CONF_CLOCK]
        sens = cg.new_Pvariable(conf[CONF_ID])
        await text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_clock(sens))

    if CONF_TIMER in config:
        conf = config[CONF_TIMER]
        sens = cg.new_Pvariable(conf[CONF_ID])
        await text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_timer(sens))

    return var