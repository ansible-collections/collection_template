.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.ieisystem.inmanage.edit_smtp_com_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ieisystem.inmanage.edit_smtp_com -- Set SMTP information
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ieisystem.inmanage collection <https://galaxy.ansible.com/ieisystem/inmanage>`_.

    To install it use: :code:`ansible-galaxy collection install ieisystem.inmanage`.

    To use it in a playbook, specify: :code:`ieisystem.inmanage.edit_smtp_com`.

.. version_added

.. versionadded:: 1.0.0 of ieisystem.inmanage

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Set SMTP com information on ieisystem Server.
- Only the M6 models support this feature.


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
                    <div class="ansibleOptionAnchor" id="parameter-asset_tag"></div>
                    <b>asset_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-asset_tag" title="Permalink to this option"></a>
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
                                            <div>product asset label,</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-email"></div>
                    <b>email</b>
                    <a class="ansibleOptionLink" href="#parameter-email" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sender email.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-event_level"></div>
                    <b>event_level</b>
                    <a class="ansibleOptionLink" href="#parameter-event_level" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>Info</li>
                                                                                                                                                                                                <li>Warning</li>
                                                                                                                                                                                                <li>Critical</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Events above this level will be sent.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
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
                                            <div>Server name.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-serial_number"></div>
                    <b>serial_number</b>
                    <a class="ansibleOptionLink" href="#parameter-serial_number" title="Permalink to this option"></a>
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
                                            <div>Serial number.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_auth"></div>
                    <b>server_auth</b>
                    <a class="ansibleOptionLink" href="#parameter-server_auth" title="Permalink to this option"></a>
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
                                            <div>SMTP server authentication.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_ip"></div>
                    <b>server_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-server_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SMTP server IP.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_password"></div>
                    <b>server_password</b>
                    <a class="ansibleOptionLink" href="#parameter-server_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SMTP server Password,lenth be 4 to 64 bits,cannot contain &#x27; &#x27;(space).</div>
                                            <div>Required when <em>server_auth=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_port"></div>
                    <b>server_port</b>
                    <a class="ansibleOptionLink" href="#parameter-server_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SMTP server port,The Identification for retry count configuration(1-65535).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_secure_port"></div>
                    <b>server_secure_port</b>
                    <a class="ansibleOptionLink" href="#parameter-server_secure_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SMTP server sesure port,The Identification for retry count configuration(1-65535).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_username"></div>
                    <b>server_username</b>
                    <a class="ansibleOptionLink" href="#parameter-server_username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SMTP server Username,lenth be 4 to 64 bits,</div>
                                            <div>must start with letters and cannot contain &#x27;,&#x27;(comma) &#x27;:&#x27;(colon) &#x27; &#x27;(space) &#x27;;&#x27;(semicolon) &#x27;\&#x27;(backslash).</div>
                                            <div>Required when <em>server_auth=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_tls_enable"></div>
                    <b>ssl_tls_enable</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_tls_enable" title="Permalink to this option"></a>
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
                                            <div>SMTP SSLTLS Enable.</div>
                                            <div><em>ssl_tls_enable=disable</em>, when <em>star_tls_enable=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-star_tls_enable"></div>
                    <b>star_tls_enable</b>
                    <a class="ansibleOptionLink" href="#parameter-star_tls_enable" title="Permalink to this option"></a>
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
                                            <div>SMTP STARTTLS Enable.</div>
                                            <div><em>star_tls_enable=disable</em>, when <em>ssl_tls_enable=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>enable</li>
                                                                                                                                                                                                <li>disable</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>SMTP Support.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-subject"></div>
                    <b>subject</b>
                    <a class="ansibleOptionLink" href="#parameter-subject" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Email theme.</div>
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

    
    - name: Smtp com test
      hosts: inmanage
      no_log: true
      connection: local
      gather_facts: no
      vars:
        inmanage:
          host: "{{ ansible_ssh_host }}"
          username: "{{ username }}"
          password: "{{ password }}"

      tasks:

      - name: "Set smtp com information"
        ieisystem.inmanage.edit_smtp_com:
          status: "disable"
          provider: "{{ inmanage }}"

      - name: "Set smtp com information"
        ieisystem.inmanage.edit_smtp_com:
          status: "enable"
          server_ip: "100.2.2.2"
          email: "ieit@ieisystem.com"
          server_auth: "enable"
          server_username: "admin"
          server_password: "1234qwer!@#$"
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

