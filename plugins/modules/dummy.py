#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# You can use this dummy module as a basis for your real module.
# See the developing modules guide for details
# https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_general.html
# There are also integration tests for the module
# in the tests/integration/targets/dummy directory.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# What you define in this section will appear on Galaxy
# and on docs.ansible.com as module documentation
# if it gets included in the Ansible package.
DOCUMENTATION = r'''
---
module: dummy

short_description: A dummy Ansible module

description:
  - Divides one number by another one and returns a quotient.

version_added: '0.1.0'

author:
  - Your name (@YourGitHubAccount)

options:
  dividend:
    description:
      - Dividend.
    type: int
    required: true

  divisor:
    description:
      - Divisor.
    type: int
    required: true
'''

EXAMPLES = r'''
- name: Divide a number by another
  register: result
  my_namespace.my_collection.dummy:
    dividend: 4
    divisor: 2

- name: Print the result
  ansible.builtin.debug:
    var: result.quotient
'''

RETURN = r'''
quotient:
  description:
  - The result of division.
  returned: on success
  sample: 2
  type: int
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    # The module accepts arguments declared here.
    argument_spec = {}
    argument_spec.update(
        dividend=dict(type='int', required=True),
        divisor=dict(type='int', required=True),
    )

    # Instantiate an object of the AnsibleModule class
    # provided by the Ansible Core.
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    # Assign passed options to variables
    dividend = module.params['dividend']
    divisor = module.params['divisor']

    # The work starts here.
    # All interactions with the user happen through
    # interfaces provided by the module object of
    # the AnsibleModule class of Ansible Core.
    # Let's fail when the divisor is zero using the fail_json() method.
    if divisor == 0:
        module.fail_json("Division by zero is not allowed!")

    # Do something.
    quotient = dividend // divisor

    # Exit the module.
    # Users will get the result in its JSON output after execution.
    module.exit_json(changed=False, quotient=quotient)


if __name__ == '__main__':
    main()
