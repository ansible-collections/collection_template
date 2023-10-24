.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.ieisystem.inmanage.edit_power_budget_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ieisystem.inmanage.edit_power_budget -- Set power budget information
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ieisystem.inmanage collection <https://galaxy.ansible.com/ieisystem/inmanage>`_.

    To install it use: :code:`ansible-galaxy collection install ieisystem.inmanage`.

    To use it in a playbook, specify: :code:`ieisystem.inmanage.edit_power_budget`.

.. version_added

.. versionadded:: 1.0.0 of ieisystem.inmanage

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Set power budget information on ieisystem Server.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- Python 3.7+
- ieisystemInManage


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>add</li>
                                                                                                                                                                                                <li>delete</li>
                                                                                                                                                                                                <li>open</li>
                                                                                                                                                                                                <li>close</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type to action.</div>
                                            <div>Required when <em>range=False</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-domain"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>system</li>
                                                                                                                                                                                                <li>cpu</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Domain id.</div>
                                            <div>Required when <em>range=False</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-end1"></div>
                    <b>end1</b>
                    <a class="ansibleOptionLink" href="#parameter-end1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, end time,must be greater than start time,from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-end2"></div>
                    <b>end2</b>
                    <a class="ansibleOptionLink" href="#parameter-end2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, end time,must be greater than start time,from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-end3"></div>
                    <b>end3</b>
                    <a class="ansibleOptionLink" href="#parameter-end3" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, end time,must be greater than start time,from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-end4"></div>
                    <b>end4</b>
                    <a class="ansibleOptionLink" href="#parameter-end4" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, end time,must be greater than start time,from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-end5"></div>
                    <b>end5</b>
                    <a class="ansibleOptionLink" href="#parameter-end5" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, end time,must be greater than start time,from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-except_action"></div>
                    <b>except_action</b>
                    <a class="ansibleOptionLink" href="#parameter-except_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>0</li>
                                                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Except action, 0 is do nothing, 1 is send alert, 2 is shutdown system, 3 is shutdown system and send alert.</div>
                                            <div>Only the M7 model supports this parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                                                                                                                                <li>4</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Policy id.</div>
                                            <div>Required when <em>range=False</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_PASSWORD</code> will be used instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-provider"></div>
                    <b>provider</b>
                    <a class="ansibleOptionLink" href="#parameter-provider" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A dict object containing connection details.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-provider/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-provider/host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-provider/password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-provider/password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_PASSWORD</code> will be used instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-provider/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-provider/username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_USERNAME</code> will be used instead.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-range"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-range" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Range of power budget watts.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start1"></div>
                    <b>start1</b>
                    <a class="ansibleOptionLink" href="#parameter-start1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, start time, from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start2"></div>
                    <b>start2</b>
                    <a class="ansibleOptionLink" href="#parameter-start2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, start time, from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start3"></div>
                    <b>start3</b>
                    <a class="ansibleOptionLink" href="#parameter-start3" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, start time, from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start4"></div>
                    <b>start4</b>
                    <a class="ansibleOptionLink" href="#parameter-start4" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add, start time, from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-start5"></div>
                    <b>start5</b>
                    <a class="ansibleOptionLink" href="#parameter-start5" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Period of add, start time, from 0 to 24.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_USERNAME</code> will be used instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-watts"></div>
                    <b>watts</b>
                    <a class="ansibleOptionLink" href="#parameter-watts" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Power budget watts of add.</div>
                                            <div>Required when <em>action=add</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-week1"></div>
                    <b>week1</b>
                    <a class="ansibleOptionLink" href="#parameter-week1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add,repetition period,the input parameters are &#x27;Mon&#x27;,&#x27;Tue&#x27;,&#x27;Wed&#x27;,&#x27;Thur&#x27;,&#x27;Fri&#x27;,&#x27;Sat&#x27;,&#x27;Sun&#x27;,separated by commas,such as Mon,Wed,Fri.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-week2"></div>
                    <b>week2</b>
                    <a class="ansibleOptionLink" href="#parameter-week2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add,repetition period,the input parameters are &#x27;Mon&#x27;,&#x27;Tue&#x27;,&#x27;Wed&#x27;,&#x27;Thur&#x27;,&#x27;Fri&#x27;,&#x27;Sat&#x27;,&#x27;Sun&#x27;,separated by commas,such as Mon,Wed,Fri.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-week3"></div>
                    <b>week3</b>
                    <a class="ansibleOptionLink" href="#parameter-week3" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add,repetition period,the input parameters are &#x27;Mon&#x27;,&#x27;Tue&#x27;,&#x27;Wed&#x27;,&#x27;Thur&#x27;,&#x27;Fri&#x27;,&#x27;Sat&#x27;,&#x27;Sun&#x27;,separated by commas,such as Mon,Wed,Fri.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-week4"></div>
                    <b>week4</b>
                    <a class="ansibleOptionLink" href="#parameter-week4" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add,repetition period,the input parameters are &#x27;Mon&#x27;,&#x27;Tue&#x27;,&#x27;Wed&#x27;,&#x27;Thur&#x27;,&#x27;Fri&#x27;,&#x27;Sat&#x27;,&#x27;Sun&#x27;,separated by commas,such as Mon,Wed,Fri.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-week5"></div>
                    <b>week5</b>
                    <a class="ansibleOptionLink" href="#parameter-week5" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Pause period of add,repetition period,the input parameters are &#x27;Mon&#x27;,&#x27;Tue&#x27;,&#x27;Wed&#x27;,&#x27;Thur&#x27;,&#x27;Fri&#x27;,&#x27;Sat&#x27;,&#x27;Sun&#x27;,separated by commas,such as Mon,Wed,Fri.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - Does not support ``check_mode``.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Power budget test
      hosts: inmanage
      connection: local
      gather_facts: no
      vars:
        inmanage:
          host: "{{ ansible_ssh_host }}"
          username: "{{ username }}"
          password: "{{ password }}"

      tasks:

      - name: "Get power budget range"
        ieisystem.inmanage.edit_power_budget:
          range: True
          provider: "{{ inmanage }}"

      - name: "add power budget"
        ieisystem.inmanage.edit_power_budget:
          action: "add"
          id: 1
          watts: 1500
          start1: 2
          end1: 5
          week1:
            - Mon
            - Wed
            - Fri
          provider: "{{ inmanage }}"

      - name: "Set power budget status to open"
        ieisystem.inmanage.edit_power_budget:
          action: "open"
          id: 1
          provider: "{{ inmanage }}"

      - name: "Set power budget status to close"
        ieisystem.inmanage.edit_power_budget:
          action: "close"
          id: 1
          provider: "{{ inmanage }}"

      - name: "Delete power budget"
        ieisystem.inmanage.edit_power_budget:
          action: "delete"
          id: 1
          provider: "{{ inmanage }}"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-changed"></div>
                    <b>changed</b>
                    <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Check to see if a change was made on the device.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-message"></div>
                    <b>message</b>
                    <a class="ansibleOptionLink" href="#return-message" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Messages returned after module execution.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#return-state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Status after module execution.</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- WangBaoshan (@ieisystem)



.. Parsing errors

