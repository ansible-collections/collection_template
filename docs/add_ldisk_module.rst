.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.ieisystem.inmanage.add_ldisk_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ieisystem.inmanage.add_ldisk -- Create logical disk
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ieisystem.inmanage collection <https://galaxy.ansible.com/ieisystem/inmanage>`_.

    To install it use: :code:`ansible-galaxy collection install ieisystem.inmanage`.

    To use it in a playbook, specify: :code:`ieisystem.inmanage.add_ldisk`.

.. version_added

.. versionadded:: 1.0.0 of ieisystem.inmanage

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create logical disk on ieisystem Server.


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
                    <div class="ansibleOptionAnchor" id="parameter-accelerator"></div>
                    <b>accelerator</b>
                    <a class="ansibleOptionLink" href="#parameter-accelerator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Driver accelerator, 1 - 1h, 2 - 2h, 3 - 3h.</div>
                                            <div>Required when <em>Info=None</em> and controller type is PMC.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-access"></div>
                    <b>access</b>
                    <a class="ansibleOptionLink" href="#parameter-access" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Access Policy, 1 - Read Write, 2 - Read Only, 3 - Blocked.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cache"></div>
                    <b>cache</b>
                    <a class="ansibleOptionLink" href="#parameter-cache" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Drive Cache, 1 - Unchanged, 2 - Enabled,3 - Disabled.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ctrl_id"></div>
                    <b>ctrl_id</b>
                    <a class="ansibleOptionLink" href="#parameter-ctrl_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Raid controller ID.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI,PMC or MV.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-info"></div>
                    <b>info</b>
                    <a class="ansibleOptionLink" href="#parameter-info" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>show</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Show controller and physical drive info.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-init"></div>
                    <b>init</b>
                    <a class="ansibleOptionLink" href="#parameter-init" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Init State, 1 - No Init, 2 - Quick Init, 3 - Full Init.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-io"></div>
                    <b>io</b>
                    <a class="ansibleOptionLink" href="#parameter-io" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>IO Policy, 1 - Direct IO, 2 - Cached IO.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-level"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-level" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>0</li>
                                                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>5</li>
                                                                                                                                                                                                <li>6</li>
                                                                                                                                                                                                <li>10</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>RAID Level, 0 - RAID0, 1 - RAID1, 5 - RAID5, 6 - RAID6, 10 - RAID10.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI or PMC.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-r"></div>
                    <b>r</b>
                    <a class="ansibleOptionLink" href="#parameter-r" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Read Policy, 1 - Read Ahead, 2 - No Read Ahead.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-select"></div>
                    <b>select</b>
                    <a class="ansibleOptionLink" href="#parameter-select" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Select Size, from 1 to 100.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
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
                                                                                                                                                                                                <li>4</li>
                                                                                                                                                                                                <li>5</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Strip Size, 0 - 32k, 1 - 64k, 2 - 128k, 3 - 256k, 4 - 512k, 5 - 1024k.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI,PMC or MV.</div>
                                            <div>When the controller type is MV,size is [0, 1].</div>
                                            <div>When the controller type is LSI or PMC,size is [1, 2, 3, 4, 5].</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-slot"></div>
                    <b>slot</b>
                    <a class="ansibleOptionLink" href="#parameter-slot" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Slot Num,input multiple slotNumber like 0,1,2....</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI or PMC.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-vname"></div>
                    <b>vname</b>
                    <a class="ansibleOptionLink" href="#parameter-vname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Virtual drive name.</div>
                                            <div>Required when <em>Info=None</em> and controller type is PMC or server model is M7.</div>
                                            <div>Required when <em>Info=None</em> and controller type is MV.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-w"></div>
                    <b>w</b>
                    <a class="ansibleOptionLink" href="#parameter-w" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1</li>
                                                                                                                                                                                                <li>2</li>
                                                                                                                                                                                                <li>3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Write Policy, 1 - Write Through, 2 - Write Back, 3 - Write caching ok if bad BBU.</div>
                                            <div>Required when <em>Info=None</em> and controller type is LSI.</div>
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

    
    - name: Add ldisk test
      hosts: inmanage
      connection: local
      gather_facts: no
      vars:
        inmanage:
          host: "{{ ansible_ssh_host }}"
          username: "{{ username }}"
          password: "{{ password }}"

      tasks:

      - name: "Show pdisk information"
        ieisystem.inmanage.add_ldisk:
          info: "show"
          provider: "{{ inmanage }}"

      - name: "Add LSI ldisk"
        ieisystem.inmanage.add_ldisk:
          ctrl_id: 0
          level: 1
          size: 1
          access: 1
          r: 1
          w: 1
          io: 1
          cache: 1
          init: 2
          select: 10
          slot: 0,1
          provider: "{{ inmanage }}"

      - name: "Add PMC ldisk"
        ieisystem.inmanage.add_ldisk:
          ctrl_id: 0
          level: 1
          size: 1
          accelerator: 1
          slot: 0,1
          vname: "test"
          provider: "{{ inmanage }}"

      - name: "Add MV ldisk"
        ieisystem.inmanage.add_ldisk:
          ctrl_id: 0
          size: 1
          vname: "test"
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

