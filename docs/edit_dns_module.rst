.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.ieisystem.inmanage.edit_dns_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ieisystem.inmanage.edit_dns -- Set dns information
++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ieisystem.inmanage collection <https://galaxy.ansible.com/ieisystem/inmanage>`_.

    To install it use: :code:`ansible-galaxy collection install ieisystem.inmanage`.

    To use it in a playbook, specify: :code:`ieisystem.inmanage.edit_dns`.

.. version_added

.. versionadded:: 1.0.0 of ieisystem.inmanage

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Set dns information on ieisystem Server.


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
                    <div class="ansibleOptionAnchor" id="parameter-dns_iface"></div>
                    <b>dns_iface</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_iface" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DNS Interface,input like &#x27;eth0&#x27;, &#x27;eth1&#x27;, &#x27;bond0&#x27;.</div>
                                            <div>Required when <em>dns_manual=auto</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_manual"></div>
                    <b>dns_manual</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_manual" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>manual</li>
                                                                                                                                                                                                <li>auto</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>DNS Settings.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_priority"></div>
                    <b>dns_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_priority" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>4</li>
                                                                                                                                                                                                <li>6</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>IP Priority.</div>
                                            <div>Required when <em>dns_manual=auto</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_server1"></div>
                    <b>dns_server1</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_server1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DNS Server1 IPv4 or IPv6 address.</div>
                                            <div>Required when <em>dns_manual=manual</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_server2"></div>
                    <b>dns_server2</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_server2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DNS Server2 IPv4 or IPv6 address.</div>
                                            <div>Required when <em>dns_manual=manual</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_server3"></div>
                    <b>dns_server3</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_server3" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DNS Server3 IPv4 or IPv6 address.</div>
                                            <div>Required when <em>dns_manual=manual</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_status"></div>
                    <b>dns_status</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>enable</li>
                                                                                                                                                                                                <li>disable</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>DNS status.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-domain_iface"></div>
                    <b>domain_iface</b>
                    <a class="ansibleOptionLink" href="#parameter-domain_iface" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network Interface,input like &#x27;eth0_v4&#x27;, &#x27;eth0_v6&#x27;, &#x27;eth1_v4&#x27;, &#x27;eth1_v6&#x27;, &#x27;bond0_v4&#x27;, &#x27;bond0_v6&#x27;.</div>
                                            <div>Required when <em>domain_manual=auto</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-domain_manual"></div>
                    <b>domain_manual</b>
                    <a class="ansibleOptionLink" href="#parameter-domain_manual" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>manual</li>
                                                                                                                                                                                                <li>auto</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Domain Settings.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-domain_name"></div>
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#parameter-domain_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Domain Name.</div>
                                            <div>Required when <em>domain_manual=manual</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-host_cfg"></div>
                    <b>host_cfg</b>
                    <a class="ansibleOptionLink" href="#parameter-host_cfg" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>manual</li>
                                                                                                                                                                                                <li>auto</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Host Settings.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Host Name.</div>
                                            <div>Required when <em>host_cfg=manual</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-register_status1"></div>
                    <b>register_status1</b>
                    <a class="ansibleOptionLink" href="#parameter-register_status1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>enable</li>
                                                                                                                                                                                                <li>disable</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>BMC register status 1.</div>
                                            <div>Only the M6 model supports this parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-register_status2"></div>
                    <b>register_status2</b>
                    <a class="ansibleOptionLink" href="#parameter-register_status2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>enable</li>
                                                                                                                                                                                                <li>disable</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>BMC register status 2.</div>
                                            <div>Only the M6 model supports this parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-registration_method1"></div>
                    <b>registration_method1</b>
                    <a class="ansibleOptionLink" href="#parameter-registration_method1" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>nsupdate</li>
                                                                                                                                                                                                <li>dhcp</li>
                                                                                                                                                                                                <li>hostname</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Registration method 1.</div>
                                            <div>Only the M6 model supports this parameter.</div>
                                            <div>Required when <em>register_status1=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-registration_method2"></div>
                    <b>registration_method2</b>
                    <a class="ansibleOptionLink" href="#parameter-registration_method2" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>nsupdate</li>
                                                                                                                                                                                                <li>dhcp</li>
                                                                                                                                                                                                <li>hostname</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Registration method 2.</div>
                                            <div>Only the M6 model supports this parameter.</div>
                                            <div>Required when <em>register_status2=enable</em>.</div>
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

    
    - name: DNS test
      hosts: inmanage
      connection: local
      gather_facts: no
      vars:
        inmanage:
          host: "{{ ansible_ssh_host }}"
          username: "{{ username }}"
          password: "{{ password }}"

      tasks:

      - name: "Set dns information"
        ieisystem.inmanage.edit_dns:
          dns_status: "disable"
          provider: "{{ inmanage }}"

      - name: "Set dns information"
        ieisystem.inmanage.edit_dns:
          dns_status: "enable"
          host_cfg: "manual"
          host_name: "123456789"
          domain_manual: "auto"
          domain_iface: "eth0_v4"
          dns_manual: "manual"
          dns_server1: "100.2.2.2"
          dns_server2: "100.2.2.3"
          dns_server3: "100.2.2.4"
          provider: "{{ inmanage }}"

      - name: "Set dns information"
        ieisystem.inmanage.edit_dns:
          dns_status: "enable"
          host_cfg: "manual"
          host_name: "123456789"
          domain_manual: "manual"
          domain_name: "test.com"
          dns_manual: "auto"
          dns_iface: "eth0"
          dns_priority: "4"
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

